# ============================================================
#  ShivaClips - i18n  (TR / EN)
# ============================================================
import os, json

_BASE = os.path.dirname(os.path.abspath(__file__))
_LANG_FILE = os.path.join(_BASE, "lang.json")

def _detect_lang() -> str:
    if os.path.exists(_LANG_FILE):
        try:
            with open(_LANG_FILE, "r", encoding="utf-8") as f:
                return json.load(f).get("lang", "en").lower()
        except Exception:
            pass
    return "en"

LANG = _detect_lang()   # "tr" or "en"

_STRINGS: dict = {

    # ── Genel ─────────────────────────────────────────────────
    "app_slogan": {
        "tr": "Klip Kaydedici — Her Oyun",
        "en": "Clip Recorder — Any Game",
    },
    "made_by": {
        "tr": "MrShivada Tarafından Kamu Hizmeti İçin",
        "en": "Made By MrShivada For Public Service",
    },

    # ── Sidebar / Nav ─────────────────────────────────────────
    "nav_dashboard": {"tr": "Ana Panel",   "en": "Dashboard"},
    "nav_clips":     {"tr": "Klipler",     "en": "Clips"},
    "nav_settings":  {"tr": "Ayarlar",     "en": "Settings"},
    "nav_about":     {"tr": "Hakkında",    "en": "About"},

    "no_game":       {"tr": "Oyun bulunamadı", "en": "No game detected"},
    "game_detected": {"tr": "Oyun aktif",      "en": "Game detected"},

    "status_idle":     {"tr": "● Boşta",          "en": "● Idle"},
    "status_warming":  {"tr": "⏳ Isınıyor...",    "en": "⏳ Warming..."},
    "status_active":   {"tr": "● Aktif",           "en": "● Active"},
    "status_stopping": {"tr": "⏳ Durduruluyor...", "en": "⏳ Stopping..."},
    "clipping":        {"tr": "⚡ Klip Alındı!",    "en": "⚡ Clipping!"},

    # ── Dashboard ─────────────────────────────────────────────
    "hero_idle":     {"tr": "KAYDA HAZIR",       "en": "READY TO CLIP"},
    "hero_warming":  {"tr": "ISINILIYOR...",      "en": "WARMING UP..."},
    "hero_running":  {"tr": "KAYIT AKTİF",        "en": "RECORDING ACTIVE"},
    "hero_stopping": {"tr": "DURDURULUYOR...",    "en": "STOPPING..."},

    "hero_sub_idle":     {"tr": "Engine'i başlat ve anında klip almak için hotkey'e bas.",
                          "en": "Start the engine and press your hotkey to clip any moment."},
    "hero_sub_warming":  {"tr": "Buffer dolduruluyor, lütfen bekleyin...",
                          "en": "Buffer filling up, please wait..."},
    "hero_sub_running":  {"tr": "Kayıt devam ediyor. Son {s}sn'yi kaydetmek için {k} bas.",
                          "en": "Recording. Press {k} to save the last {s}s."},
    "hero_sub_stopping": {"tr": "Kayıt durduruluyor...",
                          "en": "Stopping recording..."},

    "badge_idle":     {"tr": "Boşta",                       "en": "Idle"},
    "badge_warming":  {"tr": "Isınıyor ({s}sn)...",         "en": "Warming ({s}s)..."},
    "badge_running":  {"tr": "Aktif — {k} ile klip al",     "en": "Active — press {k} to clip"},
    "badge_stopping": {"tr": "Durduruluyor...",             "en": "Stopping..."},

    "stat_clips":   {"tr": "Klip",      "en": "Clips"},
    "stat_buffer":  {"tr": "Buffer",    "en": "Buffer"},
    "stat_fps":     {"tr": "FPS",       "en": "FPS"},
    "stat_hotkey":  {"tr": "Hotkey",    "en": "Hotkey"},

    "buf_label":    {"tr": "Buffer Doluluk", "en": "Buffer Fill"},
    "live_log":     {"tr": "Canlı Log",      "en": "Live Log"},
    "clear":        {"tr": "Temizle",        "en": "Clear"},
    "quick_actions":{"tr": "Hızlı İşlemler","en": "Quick Actions"},
    "clip_hotkey_label": {"tr": "KLİP HOTKEY",    "en": "CLIP HOTKEY"},
    "clip_saves_last":   {"tr": "Son {s}sn kaydeder", "en": "Saves last {s}s"},
    "clip_now_btn":      {"tr": "⚡  Şimdi Klip Al",  "en": "⚡  Clip Now"},
    "open_folder_btn":   {"tr": "📁  Klip Klasörünü Aç", "en": "📁  Open Clips Folder"},

    "pw_start":    {"tr": "Başlatmak için tıkla", "en": "Click to start"},
    "pw_warming":  {"tr": "Isınıyor...",           "en": "Warming up..."},
    "pw_stop":     {"tr": "Durdurmak için tıkla",  "en": "Click to stop"},
    "pw_stopping": {"tr": "Durduruluyor...",        "en": "Stopping..."},

    "btn_start":   {"tr": "BAŞLAT",  "en": "START"},
    "btn_warming": {"tr": "ISINIM",  "en": "WARMING"},
    "btn_stop":    {"tr": "DURDUR",  "en": "STOP"},

    "log_engine_starting": {"tr": "Engine başlatılıyor... ({k} kaydediliyor)",
                            "en": "Starting engine... (registering {k})"},
    "log_stopping":        {"tr": "Durduruluyor...",       "en": "Stopping..."},
    "log_clip_btn":        {"tr": "⚡ Klip tetiklendi (buton)", "en": "⚡ Clip triggered (button)"},
    "log_not_running":     {"tr": "⚠ Engine çalışmıyor. Önce BAŞLAT'a bas.",
                            "en": "⚠ Engine not running. Click START first."},
    "log_clip_trigger":    {"tr": "⚡ [{ts}] Son {s}sn kliplanıyor...",
                            "en": "⚡ [{ts}] Clipping last {s}s..."},
    "log_saved":           {"tr": "✅ Kaydedildi: {f} ({d:.1f}sn)",
                            "en": "✅ Saved: {f} ({d:.1f}s)"},
    "log_empty":           {"tr": "⚠ Klip boş — buffer henüz dolmamış",
                            "en": "⚠ Empty clip — buffer not full yet"},
    "log_err_writer":      {"tr": "❌ VideoWriter açılamadı",
                            "en": "❌ VideoWriter failed to open"},
    "log_err_empty":       {"tr": "❌ Dosya oluşturuldu ama boş",
                            "en": "❌ File created but empty"},
    "log_err_final":       {"tr": "❌ Son doğrulama başarısız",
                            "en": "❌ Final validation failed"},

    # ── Toast Bildirimleri ────────────────────────────────────
    "toast_clipping_title":   {"tr": "⚡ Klip alınıyor...",       "en": "⚡ Clip recording..."},
    "toast_clipping_sub":     {"tr": "Kaydediliyor, bekleyin",    "en": "Saving, please wait"},
    "toast_saved_title":      {"tr": "✅ Klip başarıyla kaydedildi!", "en": "✅ Clip saved successfully!"},
    "toast_failed_title":     {"tr": "❌ Klip kaydedilemedi",      "en": "❌ Clip save failed"},
    "toast_failed_sub":       {"tr": "Hata: {s}",                 "en": "Status: {s}"},

    # ── Clips Tab ─────────────────────────────────────────────
    "clips_title":     {"tr": "Klipler",    "en": "Clips"},
    "refresh_btn":     {"tr": "🔄 Yenile",  "en": "🔄 Refresh"},
    "open_folder":     {"tr": "📁 Klasörü Aç","en": "📁 Open Folder"},
    "search_ph":       {"tr": "Klip ara...", "en": "Search clips..."},
    "clips_count":     {"tr": "{n} klip",   "en": "{n} clips"},
    "clips_empty":     {"tr": "Henüz klip yok — Engine'i başlat ve hotkey'e bas!",
                        "en": "No clips yet — start the engine and press your hotkey!"},
    "ctx_open":        {"tr": "▶  Aç",              "en": "▶  Open"},
    "ctx_folder":      {"tr": "📁  Klasörde Göster", "en": "📁  Show in Folder"},
    "ctx_delete":      {"tr": "🗑  Sil",             "en": "🗑  Delete"},
    "del_confirm":     {"tr": "Bu klibi sil?\n{name}","en": "Delete this clip?\n{name}"},
    "folder_missing":  {"tr": "Klasör bulunamadı.",  "en": "Clips folder not found."},

    # ── Settings Tab ──────────────────────────────────────────
    "settings_title":     {"tr": "Ayarlar",            "en": "Settings"},
    "sec_recording":      {"tr": "🎬  Kayıt",           "en": "🎬  Recording"},
    "sec_hotkey":         {"tr": "⌨  Klip Hotkey",      "en": "⌨  Clip Hotkey"},
    "sec_folder":         {"tr": "📁  Klip Klasörü",    "en": "📁  Clips Folder"},
    "sec_automation":     {"tr": "🤖  Otomasyon",       "en": "🤖  Automation"},
    "clip_duration_lbl":  {"tr": "Klip süresi (sn)",   "en": "Clip duration (s)"},
    "fps_lbl":            {"tr": "Kayıt FPS",           "en": "Recording FPS"},
    "hotkey_lbl":         {"tr": "Hotkey:",             "en": "Hotkey:"},
    "hotkey_hint":        {"tr": "örn: f8, f9, ctrl+shift+z",
                           "en": "e.g. f8, f9, ctrl+shift+z"},
    "save_to_lbl":        {"tr": "Kayıt yeri:",         "en": "Save to:"},
    "browse_btn":         {"tr": "Gözat",               "en": "Browse"},
    "open_btn":           {"tr": "Aç",                  "en": "Open"},
    "autostart_check":    {"tr": "Oyun tespit edilince engine otomatik başlasın",
                           "en": "Auto-start engine when a game is detected"},
    "save_btn":           {"tr": "💾  Kaydet",           "en": "💾  Save Settings"},
    "saved_title":        {"tr": "Kaydedildi ✅",        "en": "Saved ✅"},
    "saved_msg":          {"tr": "Ayarlar kaydedildi.\nHotkey değişikliği için engine'i yeniden başlatın.",
                           "en": "Settings saved.\nRestart engine for hotkey changes."},
    "folder_err":         {"tr": "Klasör oluşturulamadı:\n{e}",
                           "en": "Cannot create folder:\n{e}"},
    "select_folder_title":{"tr": "Klip klasörünü seçin",
                           "en": "Select clips folder"},

    # ── About Tab ─────────────────────────────────────────────
    "about_title":        {"tr": "Hakkında",               "en": "About"},
    "about_version":      {"tr": "Versiyon {v}",           "en": "Version {v}"},
    "features_title":     {"tr": "  Özellikler",           "en": "  Features"},
    "how_to_title":       {"tr": "  Nasıl Kullanılır?",    "en": "  How to Use"},

    "feat_1_title": {"tr": "Anında Klip",       "en": "Instant Clip"},
    "feat_1_desc":  {"tr": "Hotkey ile son N sn'yi anında kaydet",
                     "en": "Press hotkey to save the last N seconds instantly"},
    "feat_2_title": {"tr": "Her Oyun",          "en": "Any Game"},
    "feat_2_desc":  {"tr": "Belirli bir oyuna bağlı değil",
                     "en": "Works with any game, not limited to one title"},
    "feat_3_title": {"tr": "Düşük CPU",         "en": "Low CPU Impact"},
    "feat_3_desc":  {"tr": "BGRA buffer, düşük thread önceliği",
                     "en": "BGRA buffer, below-normal thread priority"},
    "feat_4_title": {"tr": "Özel Klasör",       "en": "Custom Save Path"},
    "feat_4_desc":  {"tr": "Klipler nereye kaydedilsin, sen seç",
                     "en": "Choose exactly where your clips are saved"},
    "feat_5_title": {"tr": "Toast Bildirim",    "en": "Toast Notifications"},
    "feat_5_desc":  {"tr": "Klip alınca güzel ekran bildirimi",
                     "en": "Beautiful overlay notification when clip is saved"},
    "feat_6_title": {"tr": "Otomatik Başlat",   "en": "Auto-start"},
    "feat_6_desc":  {"tr": "Oyun açılınca engine otomatik başlar",
                     "en": "Optionally auto-start when your game is detected"},

    "step_1": {"tr": "1. install.bat → bağımlılıkları yükle",
               "en": "1. Run install.bat to install dependencies"},
    "step_2": {"tr": "2. run.bat ile başlat (CMD penceresi yok)",
               "en": "2. Launch with run.bat (no CMD window)"},
    "step_3": {"tr": "3. Ayarlar → klip süresini ve hotkey'i ayarla",
               "en": "3. Settings → set clip duration and hotkey"},
    "step_4": {"tr": "4. Ayarlar → klip klasörünü seç",
               "en": "4. Settings → choose your clips save folder"},
    "step_5": {"tr": "5. Dashboard → ▶ START ile buffer'ı başlat",
               "en": "5. Dashboard → click ▶ START to begin buffering"},
    "step_6": {"tr": "6. Oyunun başla — hotkey ile klip al!",
               "en": "6. Start your game — press hotkey to clip!"},

    # ── Splash ────────────────────────────────────────────────
    "splash_msg_1": {"tr": "Başlatılıyor...",           "en": "Initializing..."},
    "splash_msg_2": {"tr": "Modüller yükleniyor...",    "en": "Loading modules..."},
    "splash_msg_3": {"tr": "Buffer hazırlanıyor...",    "en": "Preparing buffer..."},
    "splash_msg_4": {"tr": "Hotkey kaydediliyor...",    "en": "Registering hotkey..."},
    "splash_msg_5": {"tr": "Hazır!",                    "en": "Ready!"},
    "splash_sub":   {"tr": "Klip Kaydedici — Her Oyun", "en": "Clip Recorder — Any Game"},
}


def t(key: str, **fmt) -> str:
    """Dile göre string döndür. fmt parametreleriyle format uygula."""
    entry = _STRINGS.get(key)
    if entry is None:
        return key
    text = entry.get(LANG, entry.get("en", key))
    if fmt:
        try:
            text = text.format(**fmt)
        except Exception:
            pass
    return text
