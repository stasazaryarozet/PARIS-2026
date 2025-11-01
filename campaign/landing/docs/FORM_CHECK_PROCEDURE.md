# FORM CHECK PROCEDURE
**Критический элемент**: Регистрационная форма  
**Создано**: 28 октября 2025  
**Статус**: Обязательная проверка при каждом деплое

---

## IMPORTANCE

> "Ключевая техническая часть посадочной — регистрационная форма."  
> — User requirement (28.10.2025)

**WHY CRITICAL**:
- Единственный способ конверсии посетителя → клиента
- Прямой revenue impact
- Потеря данных клиента = потеря продажи
- Технические сбои не видны в аналитике, но убивают продажи

---

## ✅ AUTOMATED CHECKS (Every Deploy)

### 1. HTML Structure Validation
```bash
# Check form element exists
grep -q 'id="bookingForm"' index.html && echo "✅ Form exists"

# Check required fields
grep -q 'id="name"' index.html && echo "✅ Name field"
grep -q 'id="contact"' index.html && echo "✅ Contact field"
grep -q 'id="consent"' index.html && echo "✅ Consent checkbox"

# Check submit button
grep -q 'type="submit"' index.html && echo "✅ Submit button"
```

### 2. Endpoints Validation
```bash
# Check primary endpoint
grep -q 'https://api.parisinjanuary.ru/api/submit' index.html && echo "✅ Primary endpoint"

# Check fallback endpoint
grep -q 'https://formspree.io/f/xvgwnvkb' index.html && echo "✅ Fallback endpoint"
```

### 3. JavaScript Validation Logic
```bash
# Check validation function exists
grep -q 'function validateContact' index.html && echo "✅ Validation logic"

# Check form submission handler
grep -q 'bookingForm.addEventListener.*submit' index.html && echo "✅ Submit handler"

# Check anti-bot measures
grep -q '_honey' index.html && echo "✅ Honeypot"
grep -q '_tstart' index.html && echo "✅ Timing"
```

---

## 🧪 MANUAL TEST CHECKLIST (Post-Deploy)

### Test 1: Form Accessibility
- [ ] Navigate to https://parisinjanuary.ru
- [ ] Scroll to "Бронь" section (or click "Забронировать место")
- [ ] Form is visible and properly styled
- [ ] All labels are in Russian and correct

### Test 2: Field Validation
- [ ] Try submitting empty form → should show HTML5 validation errors
- [ ] Enter invalid email (e.g., "test") → should show custom error
- [ ] Enter invalid phone (e.g., "123") → should show custom error
- [ ] Enter valid email (e.g., "test@example.com") → validation passes
- [ ] Enter valid phone (e.g., "+79161234567") → validation passes

### Test 3: Submission Flow
- [ ] Fill all required fields with valid data
- [ ] Check consent checkbox
- [ ] Click "Забронировать место"
- [ ] Button text changes to "Отправка..."
- [ ] Button becomes disabled during submission
- [ ] Modal "Спасибо!" appears on success
- [ ] Form resets after successful submission

### Test 4: Error Handling
- [ ] Disconnect from internet
- [ ] Try submitting form
- [ ] Should see error message: "Ошибка отправки. Попробуйте позже..."
- [ ] Reconnect internet
- [ ] Retry submission → should work

### Test 5: Anti-Bot Protection
- [ ] Open DevTools → Console
- [ ] Check `_tstart` value is set on page load
- [ ] Check `_honey` field is visually hidden
- [ ] Bot submissions should be blocked (automatic)

---

## 🔍 CURRENT FORM STATE (V4)

### Configuration

**Primary Endpoint**: `https://api.parisinjanuary.ru/api/submit`
- Custom backend
- First attempt for all submissions

**Fallback Endpoint**: `https://formspree.io/f/xvgwnvkb`
- Third-party service
- Triggers only if primary fails
- Email notifications enabled

### Fields

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| `name` | text | ✅ Yes | HTML5 required |
| `contact` | text | ✅ Yes | Email OR phone regex |
| `consent` | checkbox | ✅ Yes | HTML5 required |
| `_honey` | text (hidden) | ❌ No | Anti-bot (empty = human) |
| `_tstart` | hidden | ❌ No | Anti-bot (timing check) |

### Validation Rules

**Email Regex**:
```javascript
/^[^\s@]+@[^\s@]+\.[^\s@]+$/
```

**Phone Regex**:
```javascript
/^\+?\d{10,15}$/
```
- Accepts: +79161234567, 79161234567, +33123456789
- 10-15 digits, optional leading +

### User Experience

**Success Flow**:
1. Submit → "Отправка..." (disabled button)
2. Primary endpoint success → Reset form
3. Show modal: "Спасибо! Заявка принята. С Вами свяжутся."
4. Close modal → Form ready for new submission

**Fallback Flow**:
1. Primary fails → Automatic retry to Formspree
2. Formspree success → Same success flow
3. Both fail → Error alert with email: info@parisinjanuary.ru

**Error Messages**:
- Invalid contact: "Пожалуйста, укажите корректный email или телефон"
- Submission failed: "Ошибка отправки. Попробуйте позже или напишите на info@parisinjanuary.ru"

---

## 🚨 KNOWN ISSUES & MONITORING

### Historical Issues
None currently documented. This is the baseline.

### Monitoring Recommendations
1. **Server-side**: Check primary endpoint logs daily
2. **Client-side**: Monitor Formspree dashboard for fallback usage
3. **Analytics**: Track form submission events (if GA/Yandex configured)
4. **User reports**: Any email to info@parisinjanuary.ru mentioning form issues

### Red Flags
🚨 **Immediate action required if**:
- Primary endpoint returns 500+ errors consistently
- Formspree inbox stops receiving fallback emails
- Multiple user reports of "form not working"
- Console errors visible on live site
- Submit button doesn't respond to clicks

---

## 📋 DEPLOYMENT CHECKLIST

Before deploying ANY change to `main`:

```bash
# 1. Verify form HTML unchanged (unless intentional)
git diff HEAD origin/main -- index.html | grep -A20 'id="bookingForm"'

# 2. Run all tests
python3 test_build.py
python3 test_build_edge_cases.py

# 3. Deploy
git push origin main

# 4. Wait 60 seconds for CDN

# 5. Manual form test on live site
open https://parisinjanuary.ru/#booking

# 6. Fill test data:
#    Name: Test User
#    Contact: test@example.com
#    Consent: checked
#    Submit → Should show modal

# 7. If modal shows "Спасибо!" → ✅ DEPLOY SUCCESS
# 8. If error/no modal → 🚨 ROLLBACK IMMEDIATELY
```

---

## 🛠 EMERGENCY ROLLBACK

If form is broken on production:

```bash
# 1. Identify last working commit
git log --oneline -10

# 2. Revert to last known good
git checkout <COMMIT_HASH> -- index.html

# 3. Emergency deploy
git add index.html
git commit -m "fix: emergency rollback form to working state"
ALLOW_MAIN_PUSH=1 git push origin main --no-verify

# 4. Notify user via User_Relay

# 5. Debug issue in separate branch
git checkout -b fix/form-emergency
```

---

## 📊 SUCCESS METRICS

**Form is "working" when**:
- ✅ Visually renders correctly on desktop/mobile
- ✅ Validation prevents invalid submissions
- ✅ Primary endpoint OR fallback succeeds
- ✅ Modal displays on success
- ✅ Form resets after submission
- ✅ No console errors
- ✅ User receives confirmation (via curator email)

**Form is "broken" when**:
- ❌ Not visible on page
- ❌ Submit button doesn't respond
- ❌ Both endpoints fail
- ❌ Modal doesn't appear
- ❌ Console errors block functionality
- ❌ Data never reaches curator

---

## 🔗 RELATED FILES

- `index.html` (lines 127-161, 485-584): Form HTML + JS
- `style.css`: `.booking`, `.booking-form`, `.form-group` styles
- `WEBSITE_CONTENT.md`: Form labels in `## Форма` section
- `content.js`: Generated form texts from WEBSITE_CONTENT.md

**Dependencies**:
- Primary: https://api.parisinjanuary.ru/api/submit (custom backend)
- Fallback: https://formspree.io/f/xvgwnvkb (third-party)
- CDN: CloudFlare (cache TTL affects deploy visibility)

---

**Last checked**: 28 октября 2025  
**Status**: ✅ Form operational (V4)  
**Next check**: Required on every deploy

**REMEMBER**: Always test form manually after deploying to `main`.







