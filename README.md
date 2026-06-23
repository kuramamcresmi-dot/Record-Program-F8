# OtoKayıtValo 🎯
**Valorant Headshot Otomatik Klip Kaydedici**

Headshot attığınızda otomatik olarak **önceki 15sn + sonraki 15sn**'yi MP4 olarak kaydeder.

---

## Kurulum

### 1. Gereksinimleri Yükle
```
install.bat
```
veya manuel:
```
pip install -r requirements.txt
```

### 2. Template Oluştur (İlk Kurulum)
```
python setup_templates.py
```
- Valorant'ı açın, headshot verin
- Açılan pencerede **headshot ikonunu fare ile seçin**
- ENTER ile kaydedin

### 3. Başlat
```
python main.py
```

---

## Nasıl Çalışır?

```
[Ekran] → [Circular Buffer (son 15sn)] → Headshot tespit!
                                              ↓
                               [önceki 15sn] + [sonraki 15sn]
                                              ↓
                                      clips/headshot_XXX.mp4
```

- `mss` ile saniyede 30 kare ekran görüntüsü alır
- Son 15sn RAM'deki circular buffer'da tutulur
- Kill feed bölgesi OpenCV template matching ile taranır
- Headshot ikonu bulununca kayıt tetiklenir

---

## Konfigürasyon (`config.py`)

| Ayar | Varsayılan | Açıklama |
|------|-----------|----------|
| `CLIP_BEFORE_SECONDS` | 15 | Headshot öncesi kaç sn kaydedilsin |
| `CLIP_AFTER_SECONDS` | 15 | Headshot sonrası kaç sn kaydedilsin |
| `FPS` | 30 | Kayıt FPS |
| `MATCH_THRESHOLD` | 0.72 | Tespit hassasiyeti (0.6-0.9 arası) |
| `KILLFEED_REGION` | Sağ üst | Kill feed bölgesi koordinatları |
| `HEADSHOT_COOLDOWN` | 3.0sn | Aynı headshot'u tekrar saymaması için |

---

## Sorun Giderme

**Headshot tespit edilmiyor:**
- `config.py`'de `MATCH_THRESHOLD` değerini düşürün (0.65 deneyin)
- `setup_templates.py` ile yeni template ekleyin
- `KILLFEED_REGION` koordinatlarını çözünürlüğünüze göre ayarlayın

**Video bozuk görünüyor:**
- `FOURCC = "avc1"` deneyin (H264 codec gerektirir)
- FPS'i düşürün (20-25)

**Yüksek CPU kullanımı:**
- `FPS = 20` yapın
- `config.py`'de `KILLFEED_REGION` alanını küçültün

---

## Dosya Yapısı

```
OtoKayıtValo/
├── main.py              # Ana uygulama
├── recorder.py          # Ekran kaydı + circular buffer
├── detector.py          # Headshot tespiti
├── buffer.py            # Frame buffer
├── overlay.py           # Ekran bildirimi
├── config.py            # Tüm ayarlar
├── setup_templates.py   # Template kurulum aracı
├── install.bat          # Otomatik kurulum
├── assets/              # Headshot template PNG'leri
├── clips/               # Kaydedilen MP4 klipleri
└── temp/                # Geçici dosyalar
```
