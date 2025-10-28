# Бриф для основного ИИ‑разработчика — Paris‑2026 (28.10.2025)

## Резюме

- Архитектура «Markdown → build.py → content.js → SPA» стабильна; типографика и рендер работают корректно.
- Критичные расхождения с доками: отсутствует реальная RU/AR билингвальность/RTL, SEO‑мета не синхронизируются с контентом, кэш‑бастинг не версионный.

## Сильные стороны

- Single Source of Truth: `WEBSITE_CONTENT.md` с автогенерацией «чистого JS» (без кавычек у ключей).
- Типографический движок (кавычки‑ёлочки, тире, неразрывные пробелы) применяется рекурсивно ко всем текстам.
- SPA: аккуратный рендер контента, доступность (ARIA, клавиатура), валидация формы и модальное окно «Спасибо».
- Тесты: `test_build.py` (валидирует сборку/структуру), `test_comprehensive.py` (интеграция + продакшен‑проверки).
- Git‑процесс и документация зрелые; `pre-commit.sh` регенерирует `content.js` и гоняет тесты.

## Несоответствия документации и реализации

- Билингвальность RU/AR (RTL) заявлена в README/Knowledge Graph, но в коде нет:
  - Переключателя языка, `dir="rtl"`, раздельных сборок `content.ru.js`/`content.ar.js`.
  - `WEBSITE_CONTENT_AR.md` — черновик на русском, не интегрирован в сборку/рендер.
- SEO‑мета/OG/Twitter в `<head>` статичны; не берутся из `CONTENT.meta` → рассинхронизация при обновлении контента.
- Кэш‑бастинг через `Date.now()` для `style.css`/`content.js` (хорошо для dev, плохо для prod/CDN). Нужен версионный подход.
- Доками описаны расширенные хуки/CI (commit‑msg, pre‑push, GitHub Actions), но в дереве виден только `pre-commit.sh` (проверить фактическую установку скрытых путей).

## Приоритетные действия (короткий план)

1) Реализовать RU/AR и RTL:
   - Полноценный `WEBSITE_CONTENT_AR.md` (арабский текст, структура, фронтматтер).
   - `build.py`: сборка `content.ru.js` и `content.ar.js` (или одного `content.<lang>.js` по параметру).
   - `index.html`: переключатель RU/AR, `dir="rtl"` и `lang="ar"` для AR, сохранение выбора в `localStorage`.

2) Версионный кэш‑бастинг:
   - Подключать `style.css?v=<CONTENT.meta.version>` и `content.js?v=<CONTENT.meta.version>` вместо `Date.now()`.

3) Синхронизировать SEO/OG/Twitter:
   - После загрузки `CONTENT`, обновлять `<title>`, `<meta name="description">`, `og:*`, `twitter:*`, `link[rel=canonical]`.

4) Укрепить парсер `build.py`:
   - Мягче regex для hero/дней/локаций, покрыть вариативность Markdown.
   - Добавить тесты на краевые кейсы (пустые строки, альтернативные заголовки, переносы).

5) Верифицировать hooks/CI:
   - Подтвердить `commit-msg`, `pre-push`, `.github/workflows/*` в репо и что они действительно исполняются локально/в облаке.

6) Мелкие UX/Perf:
   - Убрать `console.log` на проде (или зафлаговать). Лёгкая ленивость рендера «По дням» (не критично).

## Минимальные правки — примеры

### 1) Версионное подключение стилей и контента (вместо `Date.now()`)

```html
<script>
  (function(){
    // Если content.js подключается динамически ниже — сначала подгрузим его,
    // затем переустановим href стиля по версии, извлечённой из CONTENT.
    const loadContent = new Promise((resolve) => {
      const s = document.createElement('script');
      s.src = 'content.js?v=' + Date.now(); // временно; будет заменено после init на версию
      s.onload = resolve;
      document.head.appendChild(s);
    });

    loadContent.then(function(){
      var v = (window.CONTENT && CONTENT.meta && CONTENT.meta.version) || '1';
      var style = document.getElementById('style-link');
      if (style) style.href = 'style.css?v=' + v;

      // Переинициализируем контент‑скрипт на версионный (по желанию — опционально):
      // const s2 = document.createElement('script');
      // s2.src = 'content.js?v=' + v;
      // document.head.appendChild(s2);
      // s2.onload = init;
      // ИЛИ сразу вызвать init(), если CONTENT уже загружен:
      if (typeof init === 'function') init();
    });
  })();
</script>
```

Рекомендуется подключать сразу версионно (после внедрения версии на уровне загрузки):

```html
<script>
  (function(){
    const s = document.createElement('script');
    s.src = 'content.js?v=' + Date.now(); // на первом проходе
    s.onload = function(){
      var v = (CONTENT && CONTENT.meta && CONTENT.meta.version) || '1';
      var l = document.getElementById('style-link');
      if (l) l.href = 'style.css?v=' + v;
      init();
    };
    document.head.appendChild(s);
  })();
</script>
```

Идеально — сразу грузить по версии (без `Date.now()`), если контент известен заранее или версия прокидывается из шаблона.

### 2) Автосинхронизация SEO/OG/Twitter из `CONTENT.meta`

```javascript
function applyMetaFromContent() {
  const M = (window.CONTENT && CONTENT.meta) || {};
  if (M.title) document.title = M.title;

  const setAttr = (selector, attr, val) => {
    if (!val) return;
    const el = document.querySelector(selector);
    if (el) el.setAttribute(attr, val);
  };

  setAttr('meta[name="description"]', 'content', M.description);
  setAttr('meta[name="keywords"]', 'content', M.keywords);
  setAttr('meta[property="og:title"]', 'content', M.ogTitle || M.title);
  setAttr('meta[property="og:description"]', 'content', M.ogDescription || M.description);
  setAttr('meta[property="og:image"]', 'content', M.ogImage);
  setAttr('meta[property="og:url"]', 'content', M.url);
  setAttr('link[rel="canonical"]', 'href', M.url);
}

// В init():
// applyMetaFromContent();
```

### 3) RU/AR переключение (набросок API)

```javascript
// Предполагается наличие content.ru.js и content.ar.js
function getSavedLang() {
  return localStorage.getItem('lang') || 'ru';
}

function setLang(lang) {
  localStorage.setItem('lang', lang);
  // Перезагрузка контента соответствующим файлом + установка dir/lang на <html>
  const html = document.documentElement;
  html.setAttribute('lang', lang === 'ar' ? 'ar' : 'ru');
  html.setAttribute('dir', lang === 'ar' ? 'rtl' : 'ltr');
  // Загрузить нужный content.<lang>.js и затем init()
}
```

## Риски/углы

- Парсер `build.py` сильно зависит от формата Markdown (жёсткие regex). Любая вариация в шапке/днях/локациях может нарушить разбор. Нужны тесты на вариативность.
- Агрессивная типографика (`&nbsp;`, кавычки, тире) — осознанный выбор; проверять, чтобы не ломать встроенные HTML‑фрагменты (сейчас теги защищаются и восстанавливаются — ок).
- Продакшен‑кэш: `Date.now()` убивает CDN‑кэш. Переход на версию обязателен для производительности.

## Проверки/CI

- Убедиться, что локально установлены и исполняются: `pre-commit`, `commit-msg`, `pre-push`.
- Проверить наличие `.github/workflows` (validate/build/deploy) и их ход в Actions.
- Расширить `test_build.py` кейсами на вариативный Markdown и проверить размер/критические элементы.

## Next Steps — чеклист

- [ ] Реализация RU/AR (контент AR, сборка, переключатель, RTL).
- [ ] Версионный кэш‑бастинг для CSS/JS.
- [ ] Автосинхронизация SEO/OG/Twitter из `CONTENT.meta`.
- [ ] Тесты на вариативность парсинга (`build.py`).
- [ ] Верификация и, при необходимости, доустановка hooks/CI.
- [ ] Уборка `console.log` на продакшене.

—

Готов реализовать RU/AR, версионный кэш‑бастинг и SEO‑синхронизацию в одной ветке с короткими тестами. При необходимости — подготовлю PR и CI‑валидацию.


