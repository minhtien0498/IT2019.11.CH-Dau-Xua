import React, { useEffect, useRef, useState } from 'react';
import {
  Accessibility,
  ArrowLeft,
  ArrowRight,
  AudioLines,
  BadgeCheck,
  BookOpen,
  Bookmark,
  Camera,
  Check,
  ChevronRight,
  CircleAlert,
  Clock3,
  Download,
  Eye,
  Flashlight,
  Headphones,
  Home,
  Info,
  Languages,
  ListFilter,
  LockKeyhole,
  Map,
  MapPin,
  Menu,
  Minus,
  Pause,
  Play,
  Plus,
  QrCode,
  RotateCcw,
  Search,
  Settings2,
  ShieldCheck,
  SkipBack,
  SkipForward,
  Sparkles,
  Star,
  TicketCheck,
  UserRound,
  X,
  Zap,
} from 'lucide-react';
import { locations, premiumStops, stories, tours } from './mockData.js';

const copy = {
  vi: {
    routes: { location: 'Chọn địa điểm', explore: 'Khám phá', objects: 'Hiện vật', story: 'Câu chuyện', suggestions: 'Điểm tiếp theo', accessibility: 'Trợ năng', tours: 'Tour', premium: 'Chi tiết tour', tourProgress: 'Hành trình của bạn', premiumStop: 'Điểm trong tour', completion: 'Hoàn thành', saved: 'Đã lưu', profile: 'Cá nhân' },
    brandTagline: 'Chạm vào lịch sử',
    welcomeTitle: <>Mỗi hiện vật<br />giữ một tiếng nói.</>,
    welcomeIntro: 'Nghe những câu chuyện di sản theo cách phù hợp với bạn, tại bảo tàng hoặc từ bất kỳ đâu.',
    welcomeVisualLabel: 'MỞ ĐẦU HÀNH TRÌNH', welcomeVisualTitle: 'Âm vang trống đồng', welcomeVisualMeta: 'Hiện vật · hoa văn · ký ức cộng đồng',
    languageLabel: 'Ngôn ngữ trải nghiệm', access: 'Hỗ trợ tiếp cận', accessDesc: 'Ưu tiên mô tả hiện vật bằng chữ và chữ lớn', start: 'Bắt đầu khám phá', settings: 'Thiết lập trợ năng', free: 'Không cần đăng ký để dùng nội dung miễn phí',
    selectedLocation: 'Địa điểm đã chọn', storiesAround: 'câu chuyện mẫu trong bản thử nghiệm', scan: 'Quét mã hiện vật', scanDesc: 'Đưa camera về phía mã QR bên cạnh hiện vật', keepListening: 'Nghe câu chuyện mẫu', openPlayer: 'Mở trình phát', featured: 'Từ bộ sưu tập', seeAll: 'Xem tất cả', recommendation: 'Gợi ý cho bạn', moreTours: 'Xem các tour', todayStory: 'CÂU CHUYỆN HÔM NAY', openStory: 'Mở câu chuyện', pauseNote: 'MỘT CHI TIẾT ĐỂ DỪNG LẠI', pauseQuote: 'Có những cánh cổng không chỉ mở vào một nơi chốn, mà còn mở vào ký ức của cả một thành phố.',
    storyReady: 'Sẵn sàng phát bản đọc minh họa', storyPlaying: 'Đang phát bản đọc minh họa', storyPaused: 'Đã tạm dừng', audioDescription: 'Mô tả hiện vật', playNarration: 'Phát bản đọc minh họa', resume: 'Tiếp tục', save: 'Lưu', saved: 'Đã lưu', nextStory: 'Câu chuyện tiếp theo', storyTab: 'Câu chuyện', timeline: 'Dòng thời gian', transcript: 'Bản chép lời', sources: 'Nguồn',
    nav: { explore: 'Khám phá', tours: 'Tour', saved: 'Đã lưu', profile: 'Cá nhân' },
    trial: 'BẢN THỬ NGHIỆM · DỮ LIỆU MINH HỌA', workspaceTitle: <>Di sản gần hơn,<br />trải nghiệm mượt hơn.</>, workspaceText: 'Thiết kế đáp ứng cho điện thoại, máy tính bảng và màn hình lớn. Nội dung và giọng đọc hiện là dữ liệu minh họa.',
  },
  en: {
    routes: { location: 'Choose a place', explore: 'Explore', objects: 'Objects', story: 'Story', suggestions: 'Next stop', accessibility: 'Accessibility', tours: 'Tours', premium: 'Tour details', tourProgress: 'Your journey', premiumStop: 'Tour stop', completion: 'Complete', saved: 'Saved', profile: 'Profile' },
    brandTagline: 'Touch history',
    welcomeTitle: <>Every object<br />keeps a voice.</>,
    welcomeIntro: 'Listen to heritage stories in a way that works for you, at the museum or wherever you are.',
    welcomeVisualLabel: 'BEGIN THE JOURNEY', welcomeVisualTitle: 'Echoes of bronze drums', welcomeVisualMeta: 'Objects · patterns · shared memory',
    languageLabel: 'Experience language', access: 'Accessibility support', accessDesc: 'Object descriptions in text and larger type', start: 'Start exploring', settings: 'Accessibility settings', free: 'No account is needed for free stories',
    selectedLocation: 'Selected location', storiesAround: 'sample stories in this prototype', scan: 'Scan an object code', scanDesc: 'Point your camera at the QR code beside an object', keepListening: 'Listen to a sample story', openPlayer: 'Open player', featured: 'From the collection', seeAll: 'See all', recommendation: 'Recommended for you', moreTours: 'Browse tours', todayStory: 'TODAY’S STORY', openStory: 'Open story', pauseNote: 'A DETAIL WORTH PAUSING FOR', pauseQuote: 'Some gateways open not only onto a place, but into the memory of an entire city.',
    storyReady: 'English sample narration is ready', storyPlaying: 'Playing sample narration', storyPaused: 'Paused', audioDescription: 'Object description', playNarration: 'Play sample narration', resume: 'Resume', save: 'Save', saved: 'Saved', nextStory: 'Next story', storyTab: 'Story', timeline: 'Timeline', transcript: 'Transcript', sources: 'Sources',
    nav: { explore: 'Explore', tours: 'Tours', saved: 'Saved', profile: 'Profile' },
    trial: 'PROTOTYPE · SAMPLE CONTENT', workspaceTitle: <>Heritage, made closer.<br />Built to flow.</>, workspaceText: 'A responsive experience for phones, tablets, and larger screens. Content and voice tracks are sample material.',
  },
};

function localStory(story, language) {
  return language === 'en' ? { ...story, ...story.en, audio: story.audioEn } : story;
}

function useAudioPlayer(source, rate = 1, language = 'vi') {
  const [playing, setPlaying] = useState(false);
  const [currentTime, setCurrentTime] = useState(0);
  const [duration, setDuration] = useState(0);
  const [error, setError] = useState('');
  const audioRef = useRef(null);

  useEffect(() => {
    const audio = new Audio(source);
    audio.preload = 'metadata';
    audio.playbackRate = rate;
    const updateTime = () => setCurrentTime(audio.currentTime);
    const updateDuration = () => setDuration(Number.isFinite(audio.duration) ? audio.duration : 0);
    const handlePlay = () => { setPlaying(true); setError(''); };
    const handlePause = () => setPlaying(false);
    const handleEnded = () => { setPlaying(false); setCurrentTime(audio.duration || 0); };
    const handleError = () => { setPlaying(false); setError(language === 'en' ? 'The sample audio could not be loaded.' : 'Không thể tải file âm thanh minh họa.'); };
    audio.addEventListener('timeupdate', updateTime);
    audio.addEventListener('loadedmetadata', updateDuration);
    audio.addEventListener('durationchange', updateDuration);
    audio.addEventListener('play', handlePlay);
    audio.addEventListener('pause', handlePause);
    audio.addEventListener('ended', handleEnded);
    audio.addEventListener('error', handleError);
    audioRef.current = audio;
    return () => {
      audio.pause();
      audio.removeEventListener('timeupdate', updateTime);
      audio.removeEventListener('loadedmetadata', updateDuration);
      audio.removeEventListener('durationchange', updateDuration);
      audio.removeEventListener('play', handlePlay);
      audio.removeEventListener('pause', handlePause);
      audio.removeEventListener('ended', handleEnded);
      audio.removeEventListener('error', handleError);
      audio.removeAttribute('src');
      audio.load();
      audioRef.current = null;
    };
  }, [source, language]);

  useEffect(() => {
    if (audioRef.current) audioRef.current.playbackRate = rate;
  }, [rate]);

  const toggle = async () => {
    const audio = audioRef.current;
    if (!audio) return;
    if (playing) {
      audio.pause();
      return;
    }
    if (duration && audio.currentTime >= duration) audio.currentTime = 0;
    try {
      await audio.play();
    } catch {
      setError(language === 'en' ? 'The browser blocked playback. Please press play again.' : 'Trình duyệt đã chặn phát âm thanh. Hãy nhấn nút phát lại.');
    }
  };

  const seekSeconds = (amount) => {
    const audio = audioRef.current;
    if (!audio) return;
    audio.currentTime = Math.min(duration || audio.duration || 0, Math.max(0, audio.currentTime + amount));
    setCurrentTime(audio.currentTime);
  };

  const seekPercent = (percent) => {
    const audio = audioRef.current;
    const total = duration || audio?.duration || 0;
    if (!audio || !total) return;
    audio.currentTime = total * percent / 100;
    setCurrentTime(audio.currentTime);
  };

  return {
    currentTime,
    duration,
    error,
    playing,
    progress: duration ? Math.min(100, currentTime / duration * 100) : 0,
    seekPercent,
    seekSeconds,
    toggle,
  };
}

function AudioPreviewButton({ source, label, language = 'vi' }) {
  const audio = useAudioPlayer(source, 1, language);
  return <button onClick={audio.toggle} aria-label={audio.playing ? (language === 'en' ? 'Pause' : 'Tạm dừng') : label}>{audio.playing ? <Pause fill="currentColor"/> : <Play fill="currentColor"/>}</button>;
}

function useDialogKeyboard(onClose, initialFocusRef) {
  const dialogRef = useRef(null);

  useEffect(() => {
    const previousFocus = document.activeElement;
    const dialog = dialogRef.current;
    window.requestAnimationFrame(() => initialFocusRef?.current?.focus() || dialog?.focus());

    const handleKeyDown = (event) => {
      if (event.key === 'Escape') {
        event.preventDefault();
        onClose();
        return;
      }
      if (event.key !== 'Tab' || !dialog) return;
      const focusable = [...dialog.querySelectorAll('button:not(:disabled), input:not(:disabled), [tabindex]:not([tabindex="-1"])')];
      if (!focusable.length) return;
      const first = focusable[0];
      const last = focusable.at(-1);
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    };

    document.addEventListener('keydown', handleKeyDown);
    return () => {
      document.removeEventListener('keydown', handleKeyDown);
      previousFocus?.focus?.();
    };
  }, [initialFocusRef, onClose]);

  return dialogRef;
}

function App() {
  const [route, setRoute] = useState('welcome');
  const [language, setLanguage] = useState('vi');
  const [history, setHistory] = useState([]);
  const [location, setLocation] = useState(locations[0]);
  const [story, setStory] = useState(stories[0]);
  const [scannerOpen, setScannerOpen] = useState(false);
  const [purchaseOpen, setPurchaseOpen] = useState(false);
  const [purchased, setPurchased] = useState(false);
  const [toast, setToast] = useState(null);
  const toastTimer = useRef(null);
  const [saved, setSaved] = useState(['camera']);
  const [settings, setSettings] = useState({
    audioDescription: true,
    haptics: true,
    highContrast: false,
    reduceMotion: false,
    fontScale: 1,
  });

  useEffect(() => {
    if (route === 'welcome') return;
    window.requestAnimationFrame(() => document.getElementById('main-content')?.focus({ preventScroll: true }));
  }, [route]);

  useEffect(() => {
    document.documentElement.lang = language;
    document.title = route === 'welcome' ? 'Dấu Xưa' : `${copy[language].routes[route] || 'Dấu Xưa'} · Dấu Xưa`;
  }, [language, route]);

  useEffect(() => () => window.clearTimeout(toastTimer.current), []);

  const text = copy[language];

  const go = (next) => {
    setHistory((items) => [...items, route]);
    setRoute(next);
    window.scrollTo({ top: 0, behavior: settings.reduceMotion ? 'auto' : 'smooth' });
  };

  const back = () => {
    const previous = history.at(-1) || 'explore';
    setHistory((items) => items.slice(0, -1));
    setRoute(previous);
    window.scrollTo({ top: 0, behavior: 'auto' });
  };

  const openStory = (item) => {
    setStory(item);
    go('story');
  };

  const announce = (message, actionLabel, onAction) => {
    window.clearTimeout(toastTimer.current);
    setToast({ message, actionLabel, onAction });
    toastTimer.current = window.setTimeout(() => setToast(null), actionLabel ? 5000 : 2600);
  };

  const toggleSaved = (id) => {
    const isSaved = saved.includes(id);
    setSaved((items) => (isSaved ? items.filter((item) => item !== id) : [...items, id]));
    announce(
      isSaved ? (language === 'en' ? 'Removed from Saved' : 'Đã bỏ khỏi mục Đã lưu') : (language === 'en' ? 'Story saved' : 'Đã lưu câu chuyện'),
      language === 'en' ? 'Undo' : 'Hoàn tác',
      () => setSaved((items) => (isSaved ? [...new Set([...items, id])] : items.filter((item) => item !== id))),
    );
  };

  const content = {
    location: <LocationPage selected={location} onConfirm={(item) => { setLocation(item); go('explore'); announce(language === 'en' ? `${item.name} selected` : `Đã chọn ${item.name}`); }} language={language} />,
    explore: <ExplorePage location={location} onLocation={() => go('location')} onScan={() => setScannerOpen(true)} onObjects={() => go('objects')} onStory={openStory} onTours={() => go('tours')} language={language} />,
    objects: <ObjectsPage onStory={openStory} language={language} />,
    story: <StoryPage story={story} settings={settings} saved={saved.includes(story.id)} onSave={() => toggleSaved(story.id)} onNext={() => go('suggestions')} language={language} />,
    suggestions: <SuggestionsPage current={story} onStory={openStory} onFinish={() => go('explore')} language={language} />,
    accessibility: <AccessibilityPage settings={settings} setSettings={setSettings} announce={announce} />,
    tours: <ToursPage onPremium={() => go('premium')} onStartFree={() => { openStory(stories[0]); announce(language === 'en' ? 'Free tour preview opened' : 'Đã mở điểm mẫu của tour miễn phí'); }} />,
    premium: <PremiumPreview onPurchase={() => setPurchaseOpen(true)} onFree={() => go('explore')} language={language} />,
    tourProgress: <TourProgress onStart={() => go('premiumStop')} announce={announce} />,
    premiumStop: <PremiumStop settings={settings} setSettings={setSettings} onStory={() => openStory(stories[0])} onComplete={() => go('completion')} language={language} />,
    completion: <Completion onReview={() => openStory(stories[0])} onHome={() => go('explore')} announce={announce} />,
    saved: <SavedPage items={stories.filter((item) => saved.includes(item.id))} onStory={openStory} language={language} />,
    profile: <ProfilePage onAccessibility={() => go('accessibility')} onPurchased={() => go(purchased ? 'tourProgress' : 'premium')} purchased={purchased} language={language} onLanguageChange={setLanguage} />,
  };

  const shellClass = [settings.highContrast && 'high-contrast', settings.reduceMotion && 'reduce-motion'].filter(Boolean).join(' ');

  return (
    <div className={shellClass} style={{ '--font-scale': settings.fontScale }}>
      <a className="skip-link" href="#main-content">{language === 'en' ? 'Skip to main content' : 'Bỏ qua đến nội dung chính'}</a>
      <div className="app-stage">
        <div className="app-shell">
          {route === 'welcome' ? (
            <WelcomePage onStart={() => { setHistory(['welcome']); setRoute('location'); }} onAccessibility={() => { setRoute('accessibility'); setHistory(['welcome']); }} settings={settings} setSettings={setSettings} language={language} onLanguageChange={setLanguage} />
          ) : (
            <>
              <AppHeader title={text.routes[route] || 'Dấu Xưa'} canBack={!['explore', 'tours', 'saved', 'profile'].includes(route)} onBack={back} onAccessibility={() => go('accessibility')} language={language} onLanguageChange={setLanguage} />
              <main id="main-content" className="page" tabIndex="-1">{content[route]}</main>
              {route !== 'location' && <BottomNav active={route} onNavigate={(next) => { setHistory([]); setRoute(next); window.scrollTo(0, 0); }} language={language} />}
            </>
          )}
          {scannerOpen && <ScannerModal onClose={() => setScannerOpen(false)} onObjects={() => { setScannerOpen(false); go('objects'); }} onSuccess={() => { setScannerOpen(false); openStory(stories[0]); announce('Đã nhận diện hiện vật'); }} />}
          {purchaseOpen && <PurchaseSheet onClose={() => setPurchaseOpen(false)} onSuccess={() => { setPurchaseOpen(false); setPurchased(true); go('tourProgress'); announce('Đã mô phỏng mua tour'); }} />}
          {toast && <div className="toast" role="status"><Check size={18} /><span>{toast.message}</span>{toast.actionLabel && <button onClick={() => { toast.onAction?.(); setToast(null); }}>{toast.actionLabel}</button>}</div>}
        </div>
      </div>
    </div>
  );
}

function BrandMark({ compact = false, language = 'vi' }) {
  return <div className={`brand-mark ${compact ? 'compact' : ''}`} aria-label="Dấu Xưa"><span className="brand-symbol">D</span><span><strong>Dấu Xưa</strong>{!compact && <small>{copy[language].brandTagline}</small>}</span></div>;
}

function WelcomePage({ onStart, onAccessibility, settings, setSettings, language, onLanguageChange }) {
  const text = copy[language];
  return (
    <main id="main-content" className="welcome-page" tabIndex="-1">
      <div className="welcome-visual">
        <img src="/images/bronze-drums.jpg" alt="" />
        <div className="welcome-visual-copy">
          <span>{text.welcomeVisualLabel}</span>
          <strong>{text.welcomeVisualTitle}</strong>
          <small>{text.welcomeVisualMeta}</small>
        </div>
      </div>
      <section className="welcome-content">
        <BrandMark language={language} />
        <h1>{text.welcomeTitle}</h1>
        <p>{text.welcomeIntro}</p>
        <fieldset className="language-choice">
          <legend>{text.languageLabel}</legend>
          <button className={language === 'vi' ? 'selected' : ''} onClick={() => onLanguageChange('vi')}><span>VI</span>Tiếng Việt<Check size={17}/></button>
          <button className={language === 'en' ? 'selected' : ''} onClick={() => onLanguageChange('en')}><span>EN</span>English<Check size={17}/></button>
        </fieldset>
        <label className="support-card">
          <span className="support-icon"><Accessibility /></span>
          <span><strong>{text.access}</strong><small>{text.accessDesc}</small></span>
          <input type="checkbox" checked={settings.audioDescription} onChange={(event) => setSettings({ ...settings, audioDescription: event.target.checked })} />
          <span className="switch" aria-hidden="true" />
        </label>
        <button className="button primary full" onClick={onStart}>{text.start} <ArrowRight size={19}/></button>
        <button className="button text full" onClick={onAccessibility}><Settings2 size={18}/>{text.settings}</button>
        <p className="privacy-note"><ShieldCheck size={15}/>{text.free}</p>
      </section>
    </main>
  );
}

function AppHeader({ title, canBack, onBack, onAccessibility, language, onLanguageChange }) {
  return (
    <header className="app-header">
      {canBack ? <button className="icon-button" onClick={onBack} aria-label={language === 'en' ? 'Go back' : 'Quay lại'}><ArrowLeft /></button> : <BrandMark compact language={language} />}
      {canBack && <strong className="app-title">{title}</strong>}
      <div className="header-actions"><button className="language-toggle" onClick={() => onLanguageChange(language === 'vi' ? 'en' : 'vi')} aria-label={language === 'vi' ? 'Switch to English' : 'Chuyển sang tiếng Việt'}>{language === 'vi' ? 'EN' : 'VI'}</button><button className="icon-button" onClick={onAccessibility} aria-label={language === 'en' ? 'Open accessibility settings' : 'Mở cài đặt trợ năng'}><Accessibility /></button></div>
    </header>
  );
}

function LocationPage({ selected, onConfirm, language }) {
  const english = language === 'en';
  const [query, setQuery] = useState('');
  const [candidate, setCandidate] = useState(selected);
  const [located, setLocated] = useState(false);
  const filtered = locations.filter((item) => item.name.toLowerCase().includes(query.toLowerCase()));

  const useCurrentLocation = () => {
    setCandidate(locations[0]);
    setLocated(true);
  };

  return (
    <div className="page-stack location-page">
      <div className="title-block">
        <span className="eyebrow">{english ? 'STEP 1' : 'BƯỚC 1'}</span>
        <h1>{english ? 'Where are you visiting?' : 'Bạn đang tham quan ở đâu?'}</h1>
        <p>{english ? 'Choose a place to see the objects and stories available there.' : 'Chọn đúng địa điểm để xem danh sách hiện vật và câu chuyện phù hợp.'}</p>
      </div>
      <button className="detect-location" onClick={useCurrentLocation}>
        <span><MapPin /></span>
        <span><strong>{english ? 'Use current location' : 'Dùng vị trí hiện tại'}</strong><small>{english ? 'Location permission is simulated in this prototype' : 'Quyền vị trí chỉ được mô phỏng trong bản thử nghiệm'}</small></span>
        <ChevronRight />
      </button>
      {located && <div className="location-status" role="status"><BadgeCheck/><span><strong>{english ? 'A nearby venue was found' : 'Đã tìm thấy địa điểm gần bạn'}</strong><small>Bảo tàng Dấu Xưa</small></span></div>}
      <div className="location-divider"><span>{english ? 'or search by name' : 'hoặc tìm theo tên'}</span></div>
      <label className="search-field"><Search/><span className="sr-only">{english ? 'Search places' : 'Tìm địa điểm'}</span><input value={query} onChange={(event) => setQuery(event.target.value)} placeholder={english ? 'Museum or heritage venue name' : 'Nhập tên bảo tàng hoặc di tích'} />{query && <button onClick={() => setQuery('')} aria-label={english ? 'Clear search' : 'Xóa tìm kiếm'}><X/></button>}</label>
      <div className="location-list" role="radiogroup" aria-label={english ? 'Venue list' : 'Danh sách địa điểm'}>
        {filtered.map((item) => (
          <button key={item.id} className={`location-option ${candidate.id === item.id ? 'selected' : ''}`} role="radio" aria-checked={candidate.id === item.id} onClick={() => setCandidate(item)}>
            <span className="location-pin"><MapPin/></span>
            <span><strong>{item.name}</strong><small>{item.address}</small><em>{item.storyCount} {english ? 'stories' : 'câu chuyện'} · {item.distance}</em></span>
            <span className="radio-mark">{candidate.id === item.id && <Check/>}</span>
          </button>
        ))}
      </div>
      {!filtered.length && <EmptyState icon={<Search/>} title={english ? 'No venue found' : 'Chưa tìm thấy địa điểm'} text={english ? 'Try another name or use your current location.' : 'Thử nhập một tên khác hoặc dùng vị trí hiện tại.'} />}
      <button className="button primary full location-confirm" onClick={() => onConfirm(candidate)}>{english ? 'Confirm venue' : 'Xác nhận địa điểm'} <ArrowRight/></button>
      <p className="mock-disclaimer"><Info/>{english ? 'Places in this screen are sample data.' : 'Các địa điểm trong màn hình này là dữ liệu minh họa.'}</p>
    </div>
  );
}

function ExplorePage({ location, onLocation, onScan, onObjects, onStory, onTours, language }) {
  const text = copy[language];
  const featured = localStory(stories[0], language);
  const today = localStory(stories[1], language);
  return (
    <div className="page-stack explore-page">
      <section className="location-intro">
        <div><span className="status-dot"><MapPin size={14}/>{text.selectedLocation}</span><h1>{location.name}</h1><p>{location.storyCount} {text.storiesAround}</p></div>
        <button className="map-button" onClick={onLocation} aria-label={language === 'en' ? 'Change venue' : 'Đổi địa điểm'}><Map /></button>
      </section>
      <button className="scan-hero" onClick={onScan}>
        <span className="scan-icon"><QrCode /></span>
        <span><strong>{text.scan}</strong><small>{text.scanDesc}</small></span>
        <ChevronRight />
      </button>
      <button className="editorial-feature" onClick={() => onStory(stories[1])}>
        <img src={today.image} alt="" />
        <span className="editorial-feature-shade" />
        <span className="editorial-feature-copy">
          <small>{text.todayStory}</small>
          <strong>{today.title}</strong>
          <em>{today.description}</em>
          <span>{text.openStory} <ArrowRight size={17}/></span>
        </span>
        <span className="editorial-feature-meta"><Headphones size={15}/>{today.duration}</span>
      </button>
      <section>
        <SectionHead title={text.keepListening} action={text.openPlayer} onAction={() => onStory(stories[0])} />
        <button className="continue-card" onClick={() => onStory(stories[0])}>
          <img src={stories[0].image} alt="Máy ảnh cổ màu đen" />
          <span className="continue-copy"><small>{featured.zone}</small><strong>{featured.title}</strong><em>{featured.duration} · {language === 'en' ? 'sample audio' : 'bản đọc minh họa'}</em></span>
          <span className="round-play"><Play fill="currentColor" /></span>
        </button>
      </section>
      <section>
        <SectionHead title={text.featured} action={text.seeAll} onAction={onObjects} />
        <div className="horizontal-cards">{stories.slice(2).map((item) => <StoryCard key={item.id} item={item} onClick={() => onStory(item)} language={language} />)}</div>
      </section>
      <aside className="heritage-note">
        <span>{text.pauseNote}</span>
        <blockquote>“{text.pauseQuote}”</blockquote>
        <i aria-hidden="true">DX</i>
      </aside>
      <section className="tour-callout">
        <img className="tour-callout-image" src={stories[0].image} alt="" />
        <div className="callout-icon"><Sparkles /></div>
        <div><span className="eyebrow">{text.recommendation}</span><h2>{language === 'en' ? 'Have 60 minutes?' : 'Bạn có 60 phút?'}</h2><p>{language === 'en' ? 'Take a six-stop route through quiet witnesses of history.' : 'Khám phá tuyến “Những nhân chứng thầm lặng” gồm 6 điểm.'}</p></div>
        <button className="button secondary" onClick={onTours}>{text.moreTours} <ArrowRight size={17}/></button>
      </section>
      <p className="mock-disclaimer"><Info size={15}/>Nội dung trong bản thử nghiệm là dữ liệu minh họa, chưa phải tư liệu lịch sử đã kiểm chứng.</p>
    </div>
  );
}

function SectionHead({ title, action, onAction }) {
  return <div className="section-head"><h2>{title}</h2>{action && <button onClick={onAction}>{action}<ChevronRight size={16}/></button>}</div>;
}

function StoryCard({ item, onClick, compact = false, language = 'vi' }) {
  const story = localStory(item, language);
  return (
    <button className={`story-card ${compact ? 'compact' : ''}`} onClick={onClick}>
      <span className="image-wrap"><img src={story.image} alt=""/><span className="duration"><Headphones size={14}/>{story.duration}</span></span>
      <span className="card-copy"><small>{story.zone}</small><strong>{story.title}</strong><em>{story.distance}</em></span>
    </button>
  );
}

function ObjectsPage({ onStory, language }) {
  const english = language === 'en';
  const [query, setQuery] = useState('');
  const [zone, setZone] = useState('Tất cả');
  const [simpleList, setSimpleList] = useState(false);
  const zones = [
    ['Tất cả', english ? 'All' : 'Tất cả'],
    ['Phòng Ký ức', english ? 'Memory gallery' : 'Phòng Ký ức'],
    ['Phòng Khởi nguyên', english ? 'Origins gallery' : 'Phòng Khởi nguyên'],
    ['Phòng Nhân chứng', english ? 'Witness gallery' : 'Phòng Nhân chứng'],
  ];
  const filtered = stories.filter((item) => { const story = localStory(item, language); return (zone === 'Tất cả' || item.zone === zone) && story.title.toLowerCase().includes(query.toLowerCase()); });
  return (
    <div className="page-stack objects-page">
      <div className="title-block"><span className="eyebrow">{stories.length} {english ? 'SAMPLE STORIES' : 'CÂU CHUYỆN MẪU'}</span><h1>{english ? 'Objects around you' : 'Hiện vật quanh bạn'}</h1><p>{english ? 'Search by name or browse each gallery.' : 'Tìm theo tên hoặc khám phá từng khu vực trưng bày.'}</p></div>
      <label className="search-field"><Search/><span className="sr-only">{english ? 'Search objects' : 'Tìm hiện vật'}</span><input value={query} onChange={(e) => setQuery(e.target.value)} placeholder={english ? 'Search an object...' : 'Tìm tên hiện vật...'} />{query && <button onClick={() => setQuery('')} aria-label={english ? 'Clear search' : 'Xóa tìm kiếm'}><X/></button>}</label>
      <div className="filter-row" aria-label={english ? 'Filter by gallery' : 'Lọc theo khu vực'}>{zones.map(([value, label]) => <button key={value} className={zone === value ? 'active' : ''} aria-pressed={zone === value} onClick={() => setZone(value)}>{label}</button>)}</div>
      <div className="result-line" aria-live="polite"><span>{filtered.length} {english ? 'results' : 'kết quả'}</span><button aria-pressed={simpleList} onClick={() => setSimpleList((value) => !value)}><ListFilter size={17}/>{simpleList ? (english ? 'Show images' : 'Hiện hình ảnh') : (english ? 'Simple list' : 'Danh sách đơn giản')}</button></div>
      <div className={`vertical-list ${simpleList ? 'simple' : ''}`}>{filtered.map((item, index) => { const story = localStory(item, language); return <div className="object-row" key={item.id}><button className="object-main" onClick={() => onStory(item)}>{!simpleList && <img src={story.image} alt=""/>}<span><small>0{index + 1} · {story.zone}</small><strong>{story.title}</strong><em><Headphones size={14}/>{story.duration}<i/> {story.distance}</em></span><ChevronRight/></button></div>; })}</div>
      {!filtered.length && <EmptyState icon={<Search/>} title={english ? 'No object found' : 'Chưa tìm thấy hiện vật'} text={english ? 'Try another keyword or gallery.' : 'Thử một từ khóa hoặc khu vực khác.'} />}
    </div>
  );
}

function StoryPage({ story: rawStory, settings, saved, onSave, onNext, language }) {
  const story = localStory(rawStory, language);
  const text = copy[language];
  const [speed, setSpeed] = useState(1);
  const [tab, setTab] = useState('story');
  const tabsRef = useRef([]);
  const narration = useAudioPlayer(story.audio, speed, language);
  const [minutes, seconds] = story.duration.split(':').map(Number);
  const plannedSeconds = minutes * 60 + seconds;
  const durationSeconds = narration.duration || plannedSeconds;
  const elapsedSeconds = Math.round(narration.currentTime);
  const remainingSeconds = Math.max(0, Math.round(durationSeconds - narration.currentTime));
  const formatTime = (value) => `${Math.floor(value / 60)}:${String(value % 60).padStart(2, '0')}`;

  const changeSpeed = () => {
    const next = speed === 1 ? 1.25 : speed === 1.25 ? 1.5 : 1;
    setSpeed(next);
  };

  const changeTabWithKeyboard = (event, index, tabs) => {
    if (!['ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(event.key)) return;
    event.preventDefault();
    const nextIndex = event.key === 'Home' ? 0 : event.key === 'End' ? tabs.length - 1 : (index + (event.key === 'ArrowRight' ? 1 : -1) + tabs.length) % tabs.length;
    setTab(tabs[nextIndex][0]);
    tabsRef.current[nextIndex]?.focus();
  };

  const tabs = [['story',text.storyTab],['timeline',text.timeline],['transcript',text.transcript],['source',text.sources]];

  return (
    <div className="story-page">
      <div className="story-hero"><img src={story.image} alt={story.audioDescription}/><div className="image-credit">{language === 'en' ? 'Sample image' : 'Ảnh minh họa'}</div><button className="floating-save" onClick={onSave} aria-pressed={saved}><Bookmark fill={saved ? 'currentColor' : 'none'}/><span>{saved ? text.saved : text.save}</span></button></div>
      <div className="story-content">
        <span className="eyebrow">{story.zone}</span><h1>{story.title}</h1><p className="story-deck">{story.description}</p>
        {settings.audioDescription && <div className="audio-description"><Eye/><div><strong>{text.audioDescription}</strong><p>{story.audioDescription}</p></div></div>}
        <section className="player-card" aria-label="Trình phát câu chuyện">
          <div className="wave" aria-hidden="true">{Array.from({ length: 34 }, (_, i) => <i key={i} style={{ height: `${12 + ((i * 17) % 28)}px` }} className={i < narration.progress / 3 ? 'heard' : ''}/>)}</div>
          <input className="range" type="range" min="0" max="100" value={narration.progress} onChange={(e) => narration.seekPercent(Number(e.target.value))} aria-label="Tiến trình phát" />
          <div className="time-row"><span>{formatTime(elapsedSeconds)}</span><span>-{formatTime(remainingSeconds)}</span></div>
          <div className="player-controls">
            <button onClick={changeSpeed} aria-label={`Tốc độ ${speed} lần`}>{speed}×</button>
            <button onClick={() => narration.seekSeconds(-15)} aria-label={language === 'en' ? 'Back 15 seconds' : 'Lùi 15 giây'}><SkipBack/><small>15</small></button>
            <button className="play-large" onClick={narration.toggle} aria-label={narration.playing ? (language === 'en' ? 'Pause' : 'Tạm dừng') : narration.currentTime > 0 && narration.currentTime < durationSeconds ? text.resume : text.playNarration}>{narration.playing ? <Pause fill="currentColor"/> : <Play fill="currentColor"/>}</button>
            <button onClick={() => narration.seekSeconds(15)} aria-label={language === 'en' ? 'Forward 15 seconds' : 'Tiến 15 giây'}><SkipForward/><small>15</small></button>
          </div>
          <p className={`player-status ${narration.error ? 'error' : ''}`} role="status">{narration.error || (narration.playing ? text.storyPlaying : narration.currentTime > 0 && narration.currentTime < durationSeconds ? text.storyPaused : text.storyReady)} · {language === 'en' ? 'Speed' : 'Tốc độ'} {speed}×</p>
        </section>
        <div className="story-tabs" role="tablist" aria-label={language === 'en' ? 'Story sections' : 'Các phần câu chuyện'}>{tabs.map(([id,label], index) => <button id={`tab-${id}`} aria-controls={`panel-${id}`} ref={(node) => { tabsRef.current[index] = node; }} role="tab" tabIndex={tab === id ? 0 : -1} aria-selected={tab === id} key={id} onKeyDown={(event) => changeTabWithKeyboard(event, index, tabs)} onClick={() => setTab(id)}>{label}</button>)}</div>
        <div id={`panel-${tab}`} role="tabpanel" aria-labelledby={`tab-${tab}`}><StoryTab tab={tab} story={story} language={language}/></div>
        <button className="button primary full next-story" onClick={onNext}>{text.nextStory} <ArrowRight/></button>
      </div>
    </div>
  );
}

function StoryTab({ tab, story, language }) {
  const english = language === 'en';
  if (tab === 'timeline') return <section className="article-section"><h2>{english ? 'Timeline' : 'Dòng thời gian'}</h2><p>{english ? 'Verified dates for this sample object have not been added yet.' : 'Chưa có các mốc thời gian được kiểm chứng cho hiện vật mẫu này.'}</p></section>;
  if (tab === 'transcript') return <section className="article-section"><h2>{english ? 'Text summary' : 'Tóm tắt bằng chữ'}</h2><p>{story.description}</p><p>{english ? 'A transcript matching the sample recording is still being prepared.' : 'Bản chép lời khớp với tệp đọc minh họa vẫn cần được biên soạn.'}</p></section>;
  if (tab === 'source') return <section className="article-section"><h2>{english ? 'Sources' : 'Nguồn tham khảo'}</h2><div className="source-card"><BookOpen/><div><strong>{english ? 'Sample content' : 'Nội dung minh họa'}</strong><p>{english ? 'Replace with museum sources before a real release.' : 'Cần thay bằng nguồn của bảo tàng trước khi sử dụng thật.'}</p></div></div></section>;
  return <section className="article-section"><h2>{english ? 'A moment kept' : 'Một khoảnh khắc được giữ lại'}</h2><p>{story.description} {english ? 'When we stand in front of an object, small details can make the past feel close: a scratch, a faded surface, or the way it was once carefully held.' : 'Khi ta đứng trước hiện vật, những chi tiết nhỏ giúp quá khứ trở nên gần gũi hơn: một vết xước, một lớp màu đã phai, hay cách người chủ cũ nâng niu món đồ.'}</p><blockquote>{english ? '“History sometimes begins with one small thing that has been kept.”' : '“Lịch sử đôi khi bắt đầu từ một điều rất nhỏ còn được giữ lại.”'}</blockquote><p className="mock-inline"><CircleAlert/>{english ? 'This passage is sample content for interface evaluation.' : 'Đoạn kể này là dữ liệu mẫu phục vụ đánh giá giao diện.'}</p></section>;
}

function SuggestionsPage({ current, onStory, onFinish, language }) {
  const items = stories.filter((item) => item.id !== current.id).slice(0, 3);
  const english = language === 'en';
  return <div className="page-stack suggestions-page"><div className="success-medallion"><Check/></div><div className="title-block centered"><span className="eyebrow">{english ? 'STORY COMPLETE' : 'CÂU CHUYỆN ĐÃ HOÀN THÀNH'}</span><h1>{english ? 'Where would you like to go next?' : 'Bạn muốn đi đâu tiếp?'}</h1><p>{english ? 'Three suggestions related to the story you just heard.' : 'Ba gợi ý có liên hệ với câu chuyện vừa nghe.'}</p></div><div className="suggestion-list">{items.map((item, index) => { const story = localStory(item, language); return <button key={item.id} onClick={() => onStory(item)}><span className="suggestion-number">0{index + 1}</span><img src={story.image} alt=""/><span><small>{index === 0 ? (english ? 'A related memory' : 'Cùng chủ đề ký ức') : index === 1 ? (english ? 'Near you' : 'Ở gần bạn') : (english ? 'Continue the timeline' : 'Nối tiếp dòng thời gian')}</small><strong>{story.title}</strong><em>{story.duration} · {story.distance}</em></span><ArrowRight/></button>; })}</div><button className="button secondary full" onClick={onFinish}>{english ? 'Finish exploring' : 'Kết thúc khám phá'}</button></div>;
}

function AccessibilityPage({ settings, setSettings, announce }) {
  const update = (key, value) => { setSettings({ ...settings, [key]: value }); announce('Đã cập nhật cài đặt'); };
  return <div className="page-stack accessibility-page"><div className="a11y-hero"><div><Accessibility/></div><span><strong>Trải nghiệm theo cách của bạn</strong><p>Các luồng chính đã có nhãn và thứ tự thao tác dự kiến; cần kiểm thử thực tế.</p></span></div><div className="status-card"><BadgeCheck/><span><strong>Cấu trúc hỗ trợ trình đọc màn hình</strong><small>Cần kiểm thử bằng VoiceOver và TalkBack</small></span><em>Chưa xác thực</em></div><SettingsGroup title="Âm thanh và phản hồi"><SettingToggle icon={<Eye/>} title="Mô tả hiện vật bằng chữ" description="Hiện phần mô tả trước câu chuyện" checked={settings.audioDescription} onChange={(v) => update('audioDescription', v)}/><SettingToggle icon={<Zap/>} title="Tín hiệu rung (mô phỏng)" description="Xem tùy chọn rung dự kiến" checked={settings.haptics} onChange={(v) => update('haptics', v)}/></SettingsGroup><SettingsGroup title="Hiển thị"><div className="font-setting"><div><span className="setting-icon"><Languages/></span><span><strong>Cỡ chữ</strong><small>Áp dụng cho nội dung và điều khiển</small></span></div><div className="stepper"><button onClick={() => update('fontScale', Math.max(.9, settings.fontScale - .1))} aria-label="Giảm cỡ chữ"><Minus/></button><output>{Math.round(settings.fontScale * 100)}%</output><button onClick={() => update('fontScale', Math.min(1.3, settings.fontScale + .1))} aria-label="Tăng cỡ chữ"><Plus/></button></div></div><SettingToggle icon={<Eye/>} title="Tăng tương phản" description="Làm đậm chữ và đường viền" checked={settings.highContrast} onChange={(v) => update('highContrast', v)}/><SettingToggle icon={<RotateCcw/>} title="Giảm chuyển động" description="Tắt các chuyển cảnh không cần thiết" checked={settings.reduceMotion} onChange={(v) => update('reduceMotion', v)}/></SettingsGroup><p className="a11y-note"><Info/>Không có thiết lập nào làm mất nội dung. Bạn có thể thay đổi lại bất cứ lúc nào.</p></div>;
}

function SettingsGroup({ title, children }) { return <section className="settings-group"><h2>{title}</h2><div>{children}</div></section>; }
function SettingToggle({ icon, title, description, checked, onChange }) { return <label className="setting-row"><span className="setting-icon">{icon}</span><span><strong>{title}</strong><small>{description}</small></span><input type="checkbox" checked={checked} onChange={(e) => onChange(e.target.checked)}/><span className="switch" aria-hidden="true"/></label>; }

function ToursPage({ onPremium, onStartFree }) {
  const [duration, setDuration] = useState(60);
  const filtered = tours.filter((tour) => tour.duration === duration || duration === 60 && tour.id === 'witnesses');
  return <div className="page-stack tours-page"><div className="title-block"><span className="eyebrow">LỘ TRÌNH ĐƯỢC BIÊN TẬP</span><h1>Chọn một cách khám phá</h1><p>Có bao nhiêu thời gian, Dấu Xưa sẽ gợi ý hành trình vừa đủ.</p></div><div className="duration-picker" aria-label="Chọn thời lượng">{[30,60,90].map((value) => <button className={duration === value ? 'active' : ''} onClick={() => setDuration(value)} key={value}><strong>{value}</strong><span>phút</span></button>)}</div><div className="tour-list">{filtered.map((tour) => <article className="tour-card" key={tour.id}><div className="tour-image"><img src={tour.image} alt=""/><span className={tour.label === 'Premium' ? 'premium-label' : 'free-label'}>{tour.label === 'Premium' && <Sparkles/>}{tour.label === 'Premium' ? 'Trả phí' : tour.label}</span></div><div className="tour-body"><span className="eyebrow">{tour.stops} ĐIỂM DỪNG · {tour.walking}</span><h2>{tour.title}</h2><p>{tour.description}</p><div className="tour-meta"><span><Clock3/>{tour.duration} phút</span><span><MapPin/>{tour.stops} điểm</span><strong>{tour.price}</strong></div><button className={`button full ${tour.label === 'Premium' ? 'primary' : 'secondary'}`} onClick={tour.label === 'Premium' ? onPremium : onStartFree}>{tour.label === 'Premium' ? 'Xem tour trả phí' : 'Bắt đầu miễn phí'}<ArrowRight/></button></div></article>)}</div><div className="premium-promise"><ShieldCheck/><div><strong>Nội dung cơ bản luôn miễn phí</strong><p>Mô tả hiện vật, khả năng tiếp cận và câu chuyện ngắn không bị khóa.</p></div></div></div>;
}

function PremiumPreview({ onPurchase, onFree, language }) {
  const english = language === 'en';
  return <div className="premium-preview"><div className="premium-hero"><img src={stories[0].image} alt="Antique camera in museum light"/><div className="premium-overlay"><span><Sparkles/>Premium Historical Tour</span><h1>{english ? 'Quiet witnesses' : 'Những nhân chứng thầm lặng'}</h1><p>{english ? 'Six objects. Six voices. One connected journey.' : 'Sáu hiện vật. Sáu tiếng nói. Một hành trình được kết nối.'}</p></div></div><div className="premium-content"><div className="stat-grid"><div><Clock3/><strong>60 {english ? 'min' : 'phút'}</strong><small>{english ? 'Duration' : 'Thời lượng'}</small></div><div><MapPin/><strong>6</strong><small>{english ? 'Stops' : 'Điểm dừng'}</small></div><div><Headphones/><strong>{english ? 'Offline' : 'Ngoại tuyến'}</strong><small>{english ? 'Download first' : 'Tải trước'}</small></div></div><section><span className="eyebrow">{english ? 'FREE PREVIEW' : 'NGHE THỬ MIỄN PHÍ'}</span><div className="sample-player"><AudioPreviewButton source={english ? '/audio/en/premium-intro.wav' : '/audio/premium-intro.wav'} label={english ? 'Play the introduction' : 'Nghe thử đoạn mở đầu'} language={language}/><span><strong>{english ? 'Introduction' : 'Đoạn mở đầu'}</strong><small>{english ? 'Sample narration' : 'Giọng đọc minh họa'}</small><i><b/></i></span></div></section><section><h2>{english ? 'What is included?' : 'Điều gì có trong tour?'}</h2><ul className="feature-list"><li><AudioLines/><span><strong>{english ? 'Deeper stories' : 'Câu chuyện chuyên sâu'}</strong><small>{english ? 'Longer content connecting all six stops.' : 'Nội dung dài hơn, kết nối xuyên suốt sáu điểm.'}</small></span></li><li><Camera/><span><strong>{english ? 'Space reconstruction' : 'Tái dựng không gian'}</strong><small>{english ? 'Optional AR with images and a transcript as alternatives.' : 'AR tùy chọn, luôn có ảnh và bản chép lời thay thế.'}</small></span></li><li><Download/><span><strong>{english ? 'Listen offline' : 'Nghe ngoại tuyến'}</strong><small>{english ? 'Planned feature; offline download is not active in this prototype.' : 'Tính năng tải trước dự kiến, chưa hoạt động trong bản mẫu.'}</small></span></li></ul></section><div className="price-panel"><span><small>{english ? 'One-time purchase' : 'Mua một lần'}</small><strong>49.000đ</strong></span><span>{english ? 'No recurring payment' : 'Không đăng ký định kỳ'}</span></div><button className="button primary full" onClick={onPurchase}>{english ? 'Get this tour' : 'Mua tour'} <ArrowRight/></button><button className="button text full" onClick={onFree}>{english ? 'Continue with free stories' : 'Tiếp tục bản miễn phí'}</button></div></div>;
}

function TourProgress({ onStart, announce }) {
  const [downloaded, setDownloaded] = useState(false);
  return <div className="page-stack progress-page"><div className="progress-hero"><span className="eyebrow light">TOUR TRẢ PHÍ · BẢN MẪU</span><h1>Những nhân chứng<br/>thầm lặng</h1><div className="progress-ring"><span><strong>1</strong><small>/ 6 điểm</small></span></div><div className="tour-progress-bar"><i/></div><p>Đang xem điểm mẫu đầu tiên của tuyến 6 điểm</p></div><button className={`offline-card ${downloaded ? 'done' : ''}`} onClick={() => { setDownloaded(!downloaded); announce(downloaded ? 'Đã bỏ trạng thái tải mô phỏng' : 'Đã mô phỏng tải tour'); }}><span>{downloaded ? <BadgeCheck/> : <Download/>}</span><span><strong>{downloaded ? 'Đã mô phỏng tải tour' : 'Mô phỏng tải ngoại tuyến'}</strong><small>Chưa lưu tệp để nghe khi mất mạng</small></span><ChevronRight/></button><section><SectionHead title="Lộ trình 6 điểm"/><div className="stop-list">{premiumStops.map((stop, index) => <div className={`stop-row ${stop.status}`} key={stop.title}><span>{index === 0 ? <Play fill="currentColor"/> : index + 1}</span><div><strong>{stop.title}</strong><small>{stop.time}{index === 0 ? ' · Điểm đang minh họa' : ' · Chưa có nội dung tương tác'}</small></div>{index === 0 ? <MapPin/> : <LockKeyhole/>}</div>)}</div></section><button className="button primary full sticky-action" onClick={onStart}>Mở điểm mẫu <ArrowRight/></button></div>;
}

function PremiumStop({ settings, setSettings, onStory, onComplete, language }) {
  const [arUnavailable, setArUnavailable] = useState(false);
  const [spatial, setSpatial] = useState(true);
  const story = localStory(stories[0], language);
  const english = language === 'en';
  return <div className="premium-stop"><div className="stop-visual"><img src={story.image} alt={story.audioDescription}/><span className="premium-label"><Sparkles/>{english ? 'Stop 1 / 6' : 'Điểm 1 / 6'}</span></div><div className="stop-content"><span className="eyebrow">{english ? 'QUIET WITNESSES' : 'NHỮNG NHÂN CHỨNG THẦM LẶNG'}</span><h1>{story.title}</h1><p>{story.description}</p><section className="immersive-player"><div className="sound-orbit"><span/><span/><AudioPreviewButton source={story.audio} label={english ? 'Play the story' : 'Phát câu chuyện'} language={language}/></div><strong>{english ? 'The space around a moment' : 'Không gian của một khoảnh khắc'}</strong><small>{english ? 'Sample narration · spatial audio concept' : 'Bản đọc minh họa · ý tưởng âm thanh không gian'}</small></section><div className="quick-toggles"><SettingToggle icon={<AudioLines/>} title={english ? 'Spatial sound' : 'Âm thanh không gian'} description={english ? 'Creates a sense of direction' : 'Tạo cảm giác định hướng'} checked={spatial} onChange={setSpatial}/><SettingToggle icon={<Zap/>} title={english ? 'Haptic cue (simulated)' : 'Tín hiệu rung (mô phỏng)'} description={english ? 'Planned cue at key moments' : 'Tùy chọn dự kiến tại mốc nội dung'} checked={settings.haptics} onChange={(v) => setSettings({...settings,haptics:v})}/></div>{!arUnavailable ? <section className="ar-card"><div><Camera/><span><strong>{english ? 'Rebuild the darkroom' : 'Tái dựng căn phòng tối'}</strong><small>{english ? 'AR is optional' : 'Trải nghiệm AR là tùy chọn'}</small></span></div><p>{english ? 'Place the camera in a reconstructed workspace.' : 'Đặt chiếc máy ảnh vào không gian làm việc được tái dựng.'}</p><button className="button secondary full" onClick={() => setArUnavailable(true)}>{english ? 'Open AR reconstruction' : 'Mở tái dựng AR'}</button></section> : <section className="ar-fallback" role="alert"><CircleAlert/><div><strong>{english ? 'AR is not available on this device' : 'AR không khả dụng trên thiết bị này'}</strong><p>{english ? 'You can continue with reconstructed images, sound, and a transcript.' : 'Bạn vẫn có thể tiếp tục bằng ảnh tái dựng, âm thanh và bản chép lời.'}</p></div><button className="button secondary full" onClick={onStory}><BookOpen/>{english ? 'Open story and text summary' : 'Mở câu chuyện và tóm tắt chữ'}</button></section>}<button className="button primary full" onClick={onComplete}>{english ? 'Simulate completing this tour' : 'Mô phỏng hoàn thành tour'} <ArrowRight/></button></div></div>;
}

function Completion({ onReview, onHome, announce }) {
  return <div className="completion-page"><div className="completion-top"><div className="laurel"><Star fill="currentColor"/></div><span className="eyebrow light">KẾT THÚC PHẦN MINH HỌA</span><h1>Bạn đã xem<br/>điểm mẫu đầu tiên.</h1><p>1/6 điểm được minh họa trong bản thử nghiệm</p></div><div className="completion-body"><section className="memory-card"><span>1/6</span><div><strong>Đã xem điểm mẫu</strong><small>Những nhân chứng thầm lặng</small></div><BadgeCheck/></section><section><h2>Điểm vừa khám phá</h2><div className="completed-stops"><div><span><Check/></span><p><strong>{premiumStops[0].title}</strong><small>Điểm 1 · dữ liệu minh họa</small></p></div></div></section><blockquote>“Khi một câu chuyện được lắng nghe, ký ức có thêm một người gìn giữ.”</blockquote><button className="button primary full" onClick={onReview}><RotateCcw/>Xem lại câu chuyện</button><button className="button secondary full" onClick={() => announce('Đã ghi nhận thao tác lưu tour trong bản mẫu')}><Bookmark/>Mô phỏng lưu tour</button><button className="button text full" onClick={onHome}><Home/>Về trang chủ</button></div></div>;
}

function SavedPage({ items, onStory, language }) { const english = language === 'en'; return <div className="page-stack"><div className="title-block"><span className="eyebrow">{english ? 'YOUR COLLECTION' : 'BỘ SƯU TẬP CỦA BẠN'}</span><h1>{english ? 'Things to revisit' : 'Những điều muốn nghe lại'}</h1><p>{english ? 'Sample stories saved in this session.' : 'Câu chuyện mẫu đã lưu trong phiên này.'}</p></div>{items.length ? <div className="vertical-cards">{items.map((item) => <StoryCard key={item.id} item={item} compact onClick={() => onStory(item)} language={language}/>)}</div> : <EmptyState icon={<Bookmark/>} title={english ? 'No saved stories yet' : 'Chưa có câu chuyện đã lưu'} text={english ? 'Save a story to find it here later.' : 'Nhấn Lưu tại một câu chuyện để tìm lại ở đây.'}/>}</div>; }

function ProfilePage({ onAccessibility, onPurchased, purchased, language, onLanguageChange }) {
  const english = language === 'en';
  return <div className="page-stack"><div className="profile-hero"><div className="avatar"><UserRound/></div><span><small>{english ? 'Visitor' : 'Khách tham quan'}</small><h1>{english ? 'Your experience' : 'Trải nghiệm của bạn'}</h1><p>{english ? 'Free to use, no account required.' : 'Dùng miễn phí, không cần tài khoản.'}</p></span></div><div className="profile-menu"><button onClick={onAccessibility}><Accessibility/><span><strong>{english ? 'Accessibility settings' : 'Cài đặt trợ năng'}</strong><small>{english ? 'Object description, text size, motion' : 'Mô tả hiện vật, cỡ chữ, chuyển động'}</small></span><ChevronRight/></button><button onClick={() => onLanguageChange(english ? 'vi' : 'en')}><Languages/><span><strong>{english ? 'Language' : 'Ngôn ngữ'}</strong><small>{english ? 'English' : 'Tiếng Việt'}</small></span><ChevronRight/></button><button onClick={onPurchased}><TicketCheck/><span><strong>{english ? 'Purchased content' : 'Nội dung đã mua'}</strong><small>{purchased ? (english ? '1 simulated premium tour' : '1 tour mua mô phỏng') : (english ? 'No tour purchased in this session' : 'Chưa mua tour trong phiên này')}</small></span><ChevronRight/></button><div className="profile-info"><Info/><span><strong>{english ? 'About Dấu Xưa' : 'Về Dấu Xưa'}</strong><small>{english ? 'Prototype 0.5.1 · sample data' : 'Bản thử nghiệm 0.5.1 · dữ liệu mẫu'}</small></span></div></div><p className="mock-disclaimer"><ShieldCheck/>{english ? 'Sample data is only kept for this session.' : 'Dữ liệu minh họa chỉ được lưu trong phiên hiện tại.'}</p></div>;
}

function ScannerModal({ onClose, onObjects, onSuccess }) {
  const [manual, setManual] = useState(false);
  const [code, setCode] = useState('');
  const [error, setError] = useState('');
  const closeRef = useRef(null);
  const dialogRef = useDialogKeyboard(onClose, closeRef);
  const submit = () => code.trim().toUpperCase() === 'DX-01' ? onSuccess() : setError('Không tìm thấy mã này. Hãy thử DX-01.');
  return <div ref={dialogRef} className="modal scanner-modal" role="dialog" aria-modal="true" aria-label="Quét mã hiện vật" tabIndex="-1"><div className="scanner-top"><button ref={closeRef} className="icon-button" onClick={onClose} aria-label="Đóng"><X/></button><strong>Quét mã hiện vật</strong><button className="icon-button" aria-label="Bật đèn"><Flashlight/></button></div>{manual ? <div className="manual-code"><QrCode/><h2>Nhập mã hiện vật</h2><p>Mã nằm bên dưới QR cạnh hiện vật.</p><label><span>Mã hiện vật</span><input autoFocus value={code} onChange={(e) => {setCode(e.target.value);setError('');}} onKeyDown={(e) => { if (e.key === 'Enter' && code.trim()) submit(); }} aria-describedby={error ? 'code-error' : undefined} aria-invalid={Boolean(error)} placeholder="Ví dụ: DX-01"/></label>{error && <p id="code-error" className="field-error" role="alert"><CircleAlert/>{error}</p>}<button className="button primary full" disabled={!code.trim()} onClick={submit}>Mở câu chuyện</button><button className="button text full" onClick={() => setManual(false)}>Quay lại camera</button><button className="button secondary full" onClick={onObjects}>Chọn hiện vật từ danh sách</button></div> : <><div className="camera-view"><div className="scan-corners"><span/><span/><span/><span/><div className="scan-line"/></div><p>Đặt mã QR vào giữa khung</p><small>Camera đang được mô phỏng trong bản thử nghiệm</small></div><div className="scanner-actions"><button onClick={onSuccess}><span><QrCode/></span><strong>Mô phỏng quét thành công</strong></button><button onClick={() => setManual(true)}><span><Menu/></span><strong>Nhập mã bằng tay</strong></button><button className="list-fallback" onClick={onObjects}><span><Search/></span><strong>Chọn hiện vật từ danh sách</strong></button></div></>}</div>;
}

function PurchaseSheet({ onClose, onSuccess }) {
  const [method, setMethod] = useState('card');
  const [loading, setLoading] = useState(false);
  const closeRef = useRef(null);
  const dialogRef = useDialogKeyboard(loading ? () => {} : onClose, closeRef);
  const pay = () => { setLoading(true); window.setTimeout(onSuccess, 900); };
  return <div ref={dialogRef} className="modal sheet-backdrop" role="dialog" aria-modal="true" aria-labelledby="purchase-title" aria-busy={loading} tabIndex="-1"><div className="purchase-sheet"><div className="drag-handle"/><div className="sheet-head"><div><span className="eyebrow">XÁC NHẬN MUA</span><h2 id="purchase-title">Những nhân chứng thầm lặng</h2></div><button ref={closeRef} className="icon-button" disabled={loading} onClick={onClose} aria-label="Đóng"><X/></button></div><div className="order-summary"><img src={stories[0].image} alt=""/><span><strong>Premium Historical Tour</strong><small>60 phút · 6 điểm · Dùng trọn đời</small></span><em>49.000đ</em></div><fieldset className="payment-method" disabled={loading}><legend>Phương thức thanh toán</legend><label className={method === 'card' ? 'selected' : ''}><input type="radio" name="payment" value="card" checked={method === 'card'} onChange={() => setMethod('card')}/><span className="pay-icon">••••</span><span><strong>Thẻ thanh toán</strong><small>Visa ·•••• 2406</small></span><Check/></label><label className={method === 'wallet' ? 'selected' : ''}><input type="radio" name="payment" value="wallet" checked={method === 'wallet'} onChange={() => setMethod('wallet')}/><span className="pay-icon">M</span><span><strong>Ví điện tử</strong><small>Tài khoản mô phỏng</small></span><Check/></label></fieldset><div className="total-row"><span>Tổng thanh toán</span><strong>49.000đ</strong></div><button className="button primary full" disabled={loading} onClick={pay}>{loading ? <><span className="spinner"/>Đang xử lý...</> : <>Thanh toán và bắt đầu <ArrowRight/></>}</button><p className="secure-note"><ShieldCheck/>Giao dịch mô phỏng · Không trừ tiền thật</p></div></div>;
}

function EmptyState({ icon, title, text }) { return <div className="empty-state"><div>{icon}</div><h2>{title}</h2><p>{text}</p></div>; }

function BottomNav({ active, onNavigate, language }) {
  const labels = copy[language].nav;
  const items = [
    ['explore', labels.explore, Home],
    ['tours', labels.tours, Map],
    ['saved', labels.saved, Bookmark],
    ['profile', labels.profile, UserRound],
  ];
  const group = active.startsWith('tour') || ['premium','premiumStop','completion'].includes(active) ? 'tours' : active;
  return <nav className="bottom-nav" aria-label="Điều hướng chính">{items.map(([id,label,Icon]) => <button key={id} className={group === id ? 'active' : ''} aria-current={group === id ? 'page' : undefined} onClick={() => onNavigate(id)}><Icon fill={group === id ? 'currentColor' : 'none'}/><span>{label}</span></button>)}</nav>;
}

export default App;
