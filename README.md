# El Joker Agency — الموقع

موقع تعريفي ثابت (static) لوكالة إل جوكر — ملف HTML واحد بدون أي تبعيات بناء.
الصفحة كلها عربية RTL، بأيقونات SVG مدمجة (بدون أيقونات إيموجي) وخط Amiri للعناوين مع fallback محلي.

## التشغيل محليًا

```bash
python3 -m http.server 8080 --directory .
# ثم افتح http://localhost:8080
```

## النشر على GitHub Pages

الموقع منشور من الفرع `main` في جذر المستودع:

```bash
git add . && git commit -m "site: initial deploy" && git push
gh api -X POST repos/eiad451/eljoker360/pages -f source[branch]=main -f source[path]=/
```

## أين تُعدّل البيانات

| ما تريده | المكان |
|---|---|
| رقم واتساب | ابحث عن `201147296651` (في كل روابط `wa.me`) |
| رابط صفحة فيسبوك | ابحث عن `facebook.com/share` |
| البريد الإلكتروني | ابحث عن `info@eljoker360.com` |
| نصوص الخدمات والأسئلة | الأقسام `services` / `process` / `faq` |
| بيانات SEO المنظمة | بلوك `application/ld+json` في أول الملف |

## ربط دومين مخصص

الملف `CNAME` غير مضاف حتى يُضبط الـDNS، لأن إضافته قبل ضبط الـDNS تعطّل النشر.
بعد شراء/ضبط `eljoker360.com`:

1. عند مزود الـDNS أضف سجلات `A` للجذر `@` إلى:
   `185.199.108.153` · `185.199.109.153` · `185.199.110.153` · `185.199.111.153`
2. أضف `CNAME` للسجل `www` إلى `eiad451.github.io`.
3. أنشئ ملف `CNAME` فيه سطر واحد: `eljoker360.com`
4. اضبط الدومين في إعدادات المستودع → Pages → Custom domain، وفعّل Enforce HTTPS.
5. حدّث `canonical` و`og:url` و`og:image` و`sitemap.xml` من `eiad451.github.io/eljoker360` إلى `https://eljoker360.com`.

## ربط الدومين بفيسبوك (Meta)

1. افتح [Meta Business Settings → Brand Safety → Domains](https://business.facebook.com/settings/domains) وأضف `eljoker360.com`.
2. اختر التحقق بـ`Meta-tag` أو `DNS TXT`:
   - **Meta-tag**: انسخ الوسم والصقه في `<head>` بجوار باقي وسوم `<meta>`.
   - **DNS TXT**: أضف سجل `TXT` بالقيمة من ميتا عند مزود الدومين.
3. بعد التحقق، اربط الدومين بالصفحة من نفس القسم، ثم شغّل `Link preview` من أداة [Sharing Debugger](https://developers.facebook.com/tools/debug/) لتحديث الكاش.
