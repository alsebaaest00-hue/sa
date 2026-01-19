# ⚡ Quick Reference - Codespaces

مرجع سريع للأوامر والاختصارات الأكثر استخداماً في GitHub Codespaces

## 🚀 البداية السريعة

```bash
# اختبر البيئة
python .devcontainer/test_environment.py

# عرض جميع الأوامر
make help

# إضافة API keys
nano .env
```

## 📝 أوامر التطوير الأساسية

### تشغيل التطبيق
```bash
make run-ui          # واجهة Streamlit (port 8501)
make run-api         # FastAPI backend (port 8000)
```

### الاختبار وجودة الكود
```bash
make test            # تشغيل الاختبارات
make test-coverage   # مع تقرير التغطية
make lint            # فحص الكود
make format          # تنسيق الكود
make all-checks      # كل الفحوصات معاً
```

### إدارة التبعيات
```bash
poetry install       # تثبيت التبعيات
poetry add <pkg>     # إضافة مكتبة جديدة
poetry remove <pkg>  # حذف مكتبة
poetry show          # عرض المكتبات المثبتة
poetry update        # تحديث التبعيات
```

## ⌨️ اختصارات VS Code

### عامة
- `Ctrl + Shift + P` (F1): Command Palette
- `Ctrl + \``: فتح/إغلاق Terminal
- `Ctrl + B`: إظهار/إخفاء Sidebar
- `Ctrl + J`: إظهار/إخفاء Panel

### التعديل
- `Ctrl + /`: تعليق/إلغاء تعليق
- `Shift + Alt + F`: تنسيق الملف
- `Ctrl + Space`: اقتراحات الكود
- `F2`: إعادة تسمية رمز (variable, function)

### التنقل
- `Ctrl + P`: البحث عن ملف
- `Ctrl + Shift + F`: بحث في المشروع
- `Ctrl + G`: الانتقال إلى سطر
- `F12`: الذهاب إلى تعريف

### Git
- `Ctrl + Shift + G`: فتح Source Control
- `Ctrl + Enter`: Commit
- `Ctrl + K Ctrl + P`: Push

## 🐍 Python في VS Code

### التشغيل والـ Debug
- `F5`: تشغيل مع Debugger
- `Shift + F5`: إيقاف Debugger
- `F9`: إضافة/حذف Breakpoint
- `F10`: Step Over
- `F11`: Step Into

### الاختبارات
- `Ctrl + ; Ctrl + A`: تشغيل جميع الاختبارات
- `Ctrl + ; Ctrl + C`: تشغيل الاختبار الحالي
- `Ctrl + ; Ctrl + F`: تشغيل الاختبارات الفاشلة

## 🔧 مهام Codespace الشائعة

### إدارة المنافذ
```bash
# عرض المنافذ المفتوحة
lsof -i -P -n | grep LISTEN

# إيقاف عملية على port معين
kill $(lsof -t -i:8501)
```

### متغيرات البيئة
```bash
# عرض المتغيرات
cat .env

# تعديل المتغيرات
nano .env

# تحميل المتغيرات
source .env
```

### تنظيف
```bash
make clean           # تنظيف الملفات المؤقتة
rm -rf .pytest_cache # حذف cache الاختبارات
rm -rf __pycache__   # حذف Python cache
```

## 🔍 استكشاف الأخطاء

### إعادة بناء Container
1. Command Palette (F1)
2. `Codespaces: Rebuild Container`
3. انتظر إعادة البناء

### إعادة تحميل Window
1. Command Palette (F1)
2. `Developer: Reload Window`

### التحقق من Logs
```bash
# عرض post-create logs
cat /tmp/postCreateCommand.log

# عرض Codespaces logs
gh codespace logs
```

### مشاكل شائعة
```bash
# المشكلة: Module not found
poetry install --no-interaction

# المشكلة: Port in use
kill $(lsof -t -i:8501)

# المشكلة: Pre-commit فشل
poetry run pre-commit run --all-files
```

## 🎯 نصائح الإنتاجية

### 1. استخدم Command Palette
معظم المهام متاحة عبر `F1` - ابحث عما تريد!

### 2. اختصارات مخصصة
- Settings → Keyboard Shortcuts
- ابحث وخصص حسب احتياجك

### 3. Multi-cursor
- `Alt + Click`: إضافة cursor
- `Ctrl + Alt + ↑/↓`: cursor للأعلى/الأسفل
- `Ctrl + D`: تحديد التكرار التالي

### 4. Snippets
اكتب `class` أو `def` ثم Tab - ستحصل على template جاهز!

### 5. Terminal متعدد
- `Ctrl + Shift + \``: terminal جديد
- `Ctrl + PgUp/PgDn`: التنقل بين terminals

## 📦 إدارة Codespace

### من GitHub.com
```
Settings → Codespaces
- عرض جميع Codespaces
- إيقاف/حذف Codespaces
- إدارة Secrets
```

### من VS Code
```bash
# إيقاف Codespace
gh codespace stop

# حذف Codespace
gh codespace delete

# عرض Codespaces
gh codespace list
```

## 🔐 إدارة Secrets

### إضافة Secret عام
1. GitHub → Settings → Codespaces
2. New secret
3. أضف: `REPLICATE_API_TOKEN`, `OPENAI_API_KEY`, إلخ
4. متاح في كل Codespace تلقائياً!

### في Codespace الحالي
```bash
# إضافة إلى .env
echo "API_KEY=your_key" >> .env

# أو استخدم nano
nano .env
```

## 📊 مراقبة الموارد

### استخدام المعالج والذاكرة
```bash
# معلومات النظام
htop

# استخدام الذاكرة
free -h

# مساحة القرص
df -h
```

### حجم المشروع
```bash
# حجم المشروع
du -sh .

# أكبر الملفات/المجلدات
du -h --max-depth=1 | sort -hr | head -10
```

## 🎨 تخصيص VS Code

### Themes
1. Command Palette (F1)
2. `Preferences: Color Theme`
3. اختر Theme المفضل

### Extensions إضافية
```
- Better Comments
- Bracket Pair Colorizer
- indent-rainbow
- Material Icon Theme
```

## 🌐 الوصول للتطبيق

### روابط المنافذ
- افتح تبويب "PORTS" في الأسفل
- اضغط على أيقونة الكرة الأرضية 🌐 بجانب المنفذ
- أو انسخ الرابط

### مشاركة المنفذ
- Right-click على المنفذ → Port Visibility
- اختر "Public" للمشاركة مع آخرين

## 🚨 حالات طوارئ

### Codespace معلق
```bash
# من جهازك المحلي
gh codespace rebuild
```

### فقدان التغييرات
```bash
# التأكد من الـ commits
git log

# استعادة ملف
git checkout -- <file>

# استعادة من commit سابق
git reset --hard <commit-hash>
```

### نفدت المساحة
```bash
# تنظيف شامل
make clean
poetry cache clear pypi --all
docker system prune -a
```

## 📚 موارد إضافية

- [VS Code Shortcuts PDF](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf)
- [GitHub Codespaces Docs](https://docs.github.com/codespaces)
- [Poetry Commands](https://python-poetry.org/docs/cli/)
- [Make Commands](../Makefile) - اكتب `make help`

---

**💡 Tip:** اطبع هذه الصفحة وضعها بجانبك للمرجع السريع!
