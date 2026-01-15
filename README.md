# 🎨 SA - منصة تحويل النصوص إلى وسائط متعددة

[![CI](https://github.com/alsebaaest00/sa/actions/workflows/python-ci.yml/badge.svg)](https://github.com/alsebaaest00/sa/actions/workflows/python-ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

منصة قوية وذكية لتحويل النصوص إلى صور وفيديوهات مع إضافة الصوت والموسيقى باستخدام الذكاء الاصطناعي.

> 🚀 **[بداية سريعة في 3 خطوات →](QUICKSTART.md)** | 📖 **[دليل الاستخدام الكامل →](USAGE.md)**

## ✨ المميزات

- 🖼️ **توليد الصور من النص**: إنشاء صور عالية الجودة باستخدام AI
- 🎬 **توليد الفيديو**: تحويل النصوص إلى فيديوهات أو إنشاء عروض شرائح
- 🎤 **تحويل النص إلى صوت**: صوت طبيعي بلغات متعددة
- 🎵 **إضافة الموسيقى**: دمج الأصوات المحيطة والخلفية الموسيقية
- 💡 **اقتراحات ذكية**: تحسين النصوص وتوليد أفكار جديدة
- 🎯 **مشاريع متكاملة**: إنشاء فيديوهات كاملة بسيناريو تلقائي

## 🚀 التثبيت السريع

```bash
# استنساخ المشروع
git clone https://github.com/alsebaaest00/sa.git
cd sa

# تثبيت التبعيات
poetry install

# إعداد متغيرات البيئة
cp .env.example .env
# عدّل .env وأضف مفاتيح API
```

## 🎯 الاستخدام

### تشغيل واجهة الويب

```bash
poetry run streamlit run src/sa/ui/app.py
```

ثم افتح المتصفح على: `http://localhost:8501`

### الاستخدام البرمجي

```python
from sa.generators import ImageGenerator, AudioGenerator
from sa.utils import SuggestionEngine

# توليد صورة
img_gen = ImageGenerator(api_key="your_replicate_token")
images = img_gen.generate("منظر طبيعي خلاب")

# تحويل نص إلى صوت
audio_gen = AudioGenerator(api_key="your_elevenlabs_key")
audio = audio_gen.generate_speech("مرحباً بك")

# الحصول على اقتراحات
engine = SuggestionEngine(api_key="your_openai_key")
improved = engine.improve_prompt("قطة جميلة")
```

## 📖 التوثيق

### API Keys المطلوبة

#### 1. Replicate (مطلوب للصور والفيديو)
- التسجيل: [replicate.com](https://replicate.com)
- الحصول على Token من [Settings](https://replicate.com/account)

#### 2. OpenAI (للاقتراحات الذكية)
- التسجيل: [platform.openai.com](https://platform.openai.com)
- إنشاء API Key من [Dashboard](https://platform.openai.com/api-keys)

#### 3. ElevenLabs (للصوت عالي الجودة - اختياري)
- التسجيل: [elevenlabs.io](https://elevenlabs.io)
- يمكن استخدام gTTS المجاني كبديل

## 🧪 الاختبارات

```bash
# تشغيل جميع الاختبارات
poetry run pytest

# تشغيل مع تقرير التغطية
poetry run pytest --cov=sa

# فحص جودة الكود
poetry run black --check .
poetry run ruff check .
```

## 📝 الترخيص

هذا المشروع مرخص تحت [MIT License](LICENSE).

## 🙏 شكر وتقدير

- [Replicate](https://replicate.com) - لنماذج AI
- [OpenAI](https://openai.com) - للاقتراحات الذكية
- [ElevenLabs](https://elevenlabs.io) - للصوت عالي الجودة
- [Streamlit](https://streamlit.io) - لواجهة المستخدم

---

**صُنع بـ ❤️ باستخدام Python و AI**
