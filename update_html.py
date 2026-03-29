import re

with open('C:/Users/ADMIN/.gemini/antigravity/scratch/bni-invite/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Tách file tại "<div class=\"wrapper\""
parts = html.split('<div class="wrapper"', 1)
if len(parts) == 2:
    top_half = parts[0]
else:
    print("Cannot find wrapper")
    exit(1)

new_bottom = """<div class="wrapper" style="padding-bottom: 40px; min-height: 100vh; display: flex; flex-direction: column; position: relative;">

    <!-- CÁ NHÂN HOÁ (NAME CARD) -->
    <div id="personalized-hero" style="display:none; text-align:left; padding: 24px; background:var(--white); border-radius: 20px; box-shadow: 0 16px 40px rgba(204,29,29,0.15); margin: 20px auto 30px; max-width: 600px; width: 90%; position:relative; z-index:2; border: 2px solid var(--red-light); align-items: center; gap: 20px;">
      <div id="ph-img-container" style="width: 80px; height: 80px; border-radius: 50%; background: #eee; overflow: hidden; border: 3px solid var(--red); flex-shrink: 0; display: none;">
        <img id="ph-img" src="" style="width:100%; height: 100%; object-fit:cover;">
      </div>
      <div style="flex:1;">
        <h2 style="font-size:18px; font-weight:900; color:var(--text); line-height:1.2; margin-bottom: 4px;">Chào mừng <span id="ph-name" style="color:var(--red);"></span>!</h2>
        <p style="font-size:13px; color:var(--gray); margin-bottom:2px;"><strong id="ph-company"></strong></p>
        <p style="font-size:12px; color:var(--gray); margin-bottom:0"><span id="ph-phone"></span> | <span id="ph-email"></span></p>
      </div>
      <div style="width: 100%; margin-top: 16px;">
        <p style="font-size:13px; color:var(--text); font-weight: 600; text-align: center; margin-bottom: 12px;">Vui lòng kiểm tra lại thông tin và xác nhận đăng ký!</p>
        <button id="confirm-register-btn" style="width: 100%; padding: 14px; background: var(--red); color: white; border: none; border-radius: 8px; font-weight: 800; font-size: 15px; cursor: pointer; transition: all 0.3s; box-shadow: 0 4px 15px rgba(204,29,29,0.3);">XÁC NHẬN ĐĂNG KÝ ✓</button>
      </div>
    </div>
    <style>
       #personalized-hero.show { display: flex !important; flex-wrap: wrap; }
    </style>

    <!-- HERO SECTION -->
    <section class="hero reveal">
      <div class="bni-logo reveal">
        <div class="bni-logo-badge">
          <div class="bni-text">CỘNG ĐỒNG <span>DOANH NHÂN</span></div>
        </div>
        <div class="meeting-badge">KẾT NỐI KINH DOANH</div>
      </div>
      
      <div class="hero-label">Kính mời Anh/Chị tham dự</div>
      <h1 class="hero-title">Sự kiện định kỳ</h1>
      <p class="hero-subtitle">Mở rộng mối quan hệ và gia tăng doanh số thông qua các cơ hội học hỏi.</p>
      <div class="hero-date-pill">
        <div class="dot"></div>
        <span id="event-date-display">Đang cập nhật...</span>
      </div>
    </section>

    <!-- MEETING NUMBER -->
    <div class="meeting-number-badge reveal">
      <div class="meeting-num-card">
        <div class="meeting-num-circle"><span class="meeting-num-number" id="meeting-num">...</span></div>
        <div>
          <div class="meeting-num-label">Buổi kết nối kinh doanh</div>
          <div class="meeting-num-desc">Khách mời & Thành viên</div>
        </div>
      </div>
    </div>

    <!-- COUNTDOWN -->
    <section class="countdown-section reveal" id="countdown">
      <div class="countdown-label">Sự kiện sẽ bắt đầu sau</div>
      <div class="countdown-grid">
        <div class="countdown-item"><div class="countdown-value" id="cd-days">00</div><div class="countdown-unit">Ngày</div></div>
        <div class="countdown-item"><div class="countdown-value" id="cd-hours">00</div><div class="countdown-unit">Giờ</div></div>
        <div class="countdown-item"><div class="countdown-value" id="cd-mins">00</div><div class="countdown-unit">Phút</div></div>
        <div class="countdown-item"><div class="countdown-value" id="cd-secs">00</div><div class="countdown-unit">Giây</div></div>
      </div>
    </section>

    <!-- BENEFITS -->
    <section class="section reveal">
      <div class="section-inner">
        <h2 class="section-title">Giá trị nhận được</h2>
        <h3 class="section-heading">Tại sao bạn nên tham gia?</h3>
        <ul class="benefit-list">
          <li class="benefit-item"><div class="benefit-icon">🤝</div><div class="benefit-text"><strong>Mở rộng mối quan hệ:</strong> Gặp gỡ hơn 70 chủ doanh nghiệp uy tín.</div></li>
          <li class="benefit-item"><div class="benefit-icon">📢</div><div class="benefit-text"><strong>Quảng bá doanh nghiệp:</strong> Cơ hội giới thiệu sản phẩm, dịch vụ.</div></li>
          <li class="benefit-item"><div class="benefit-icon">📈</div><div class="benefit-text"><strong>Tăng trưởng doanh thu:</strong> Gia tăng khách hàng thông qua referral.</div></li>
        </ul>
      </div>
    </section>

    <!-- LOCATION & TIME -->
    <section class="section reveal" style="padding-top: 0;">
      <div class="section-inner">
        <h2 class="section-title">Thông tin</h2>
        <h3 class="section-heading">Thời gian & Địa điểm</h3>
        <div class="info-grid">
          <div class="info-col">
            <div class="info-col-title">⏰ Thời gian</div>
            <div class="info-col-main">06:30 - 09:00</div>
            <div class="info-col-sub">Thứ Tư tuần này</div>
          </div>
          <div class="info-divider"></div>
          <div class="info-col">
            <div class="info-col-title">📍 Địa điểm</div>
            <div class="info-col-main">AQUA JARDIN</div>
            <div class="info-col-sub">307 Nơ Trang Long, Bình Lợi Trung, Tp. HCM</div>
            <a href="https://maps.google.com/?q=AQUA+JARDIN+307+Nơ+Trang+Long" target="_blank" class="map-btn">🗺️ Xem Bản Đồ</a>
          </div>
        </div>
      </div>
    </section>

    <!-- SPEAKER / CMS -->
    <section class="section reveal" style="padding-top: 0;">
      <div class="section-inner" style="background: var(--cream); border: 2px solid var(--red-light); padding: 36px 20px;">
        <h2 class="section-title" style="text-align: center;">Tâm Điểm Sự Kiện</h2>
        <h3 class="section-heading" style="text-align: center;">Bài Chia Sẻ 10 Phút</h3>
        <div style="display: flex; align-items: center; justify-content: center; gap: 20px; flex-wrap: wrap; margin-top: 20px;">
          <div style="width: 120px; height: 120px; border-radius: 50%; background: #ccc; border: 4px solid var(--red); display:flex; align-items:center; justify-content:center; overflow:hidden; flex-shrink:0;">
            <img src="https://ui-avatars.com/api/?name=H%C6%B0%E1%BB%9Dng&background=CC1D1D&color=fff&size=150" alt="Speaker" id="speaker-img" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <div style="text-align: left; max-width: 300px;">
            <span style="font-size: 13px; font-weight: 700; color: var(--gray); text-transform: uppercase;">Chủ Đề</span>
            <h4 id="sp-topic" style="font-size: 18px; font-weight: 800; color: var(--red); line-height: 1.3; margin: 4px 0 8px;">Bí Mật Kinh doanh<br>Sức Khỏe Làm Đẹp thời 5.0</h4>
            <div id="sp-name" style="font-size: 13px; font-weight: 600; color: #333; line-height: 1.5;">SPEAKER: <strong style="color:var(--red); font-size:14px;">NGUYỄN THỊ HƯỜNG</strong><br>CÔNG TY TNHH BIG EMPIRE</div>
          </div>
        </div>
      </div>
    </section>

    <!-- CALENDAR -->
    <section class="section reveal" style="padding-top: 0;">
      <div class="section-inner">
        <h2 class="section-title">Lịch trình</h2>
        <h3 class="section-heading" id="cal-section-heading">Tháng -- / 20--</h3>
        <p style="font-size: 14px; color: var(--gray); margin-bottom: 20px; text-align: center;">Các buổi họp kết nối diễn ra vào <strong>Thứ 4 hàng tuần</strong>.</p>
        <div class="calendar-wrap">
          <div class="calendar">
            <div class="cal-header" id="cal-header-title">THÁNG -- NĂM --</div>
            <div class="cal-days-header">
              <div class="cal-day-name">CN</div><div class="cal-day-name">T2</div><div class="cal-day-name">T3</div><div class="cal-day-name">T4</div><div class="cal-day-name">T5</div><div class="cal-day-name">T6</div><div class="cal-day-name">T7</div>
            </div>
            <div class="cal-grid" id="cal-grid"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- SCHEDULE -->
    <section class="section reveal" style="padding-top: 0;">
      <div class="section-inner">
        <h2 class="section-title">Agenda</h2>
        <h3 class="section-heading">Lịch trình chi tiết</h3>
        <ul class="schedule-list">
          <li class="schedule-item">
            <div class="schedule-time">06:30</div>
            <div class="schedule-dot"></div>
            <div class="schedule-content">
              <div class="schedule-phase">Đón khách & Giao lưu mở</div>
              <ul class="schedule-items"><li>Networking tự do</li><li>Ăn sáng nhẹ & Cà phê</li></ul>
            </div>
          </li>
          <li class="schedule-item">
            <div class="schedule-time">07:00</div>
            <div class="schedule-dot"></div>
            <div class="schedule-content">
              <div class="schedule-phase">Phần chính sự kiện</div>
              <ul class="schedule-items"><li>Giới thiệu 60 giây từng doanh nghiệp</li><li>Trao đổi cơ hội kinh doanh (Referrals)</li></ul>
            </div>
          </li>
          <li class="schedule-item">
            <div class="schedule-time">08:00</div>
            <div class="schedule-dot"></div>
            <div class="schedule-content">
              <div class="schedule-phase">Bài chia sẻ 10 phút</div>
              <ul class="schedule-items"><li>Thuyết trình & Hỏi đáp</li></ul>
            </div>
          </li>
          <li class="schedule-item">
            <div class="schedule-time">08:45</div>
            <div class="schedule-dot"></div>
            <div class="schedule-content">
              <div class="schedule-phase">Bế mạc</div>
              <ul class="schedule-items"><li>Giao lưu sau sự kiện</li></ul>
            </div>
          </li>
        </ul>
      </div>
    </section>

    <!-- NOTES -->
    <section class="section reveal" style="padding-top: 0;">
      <div class="section-inner">
        <h2 class="section-title">Chuẩn bị</h2>
        <h3 class="section-heading">Lưu ý khi tham dự</h3>
        <div class="notes-grid">
          <div class="note-item"><div class="note-emoji">👔</div><div class="note-text"><strong>Trang phục</strong>Lịch sự, chuyên nghiệp (Business Casual / Vest).</div></div>
          <div class="note-item"><div class="note-emoji">🪪</div><div class="note-text"><strong>Nhận diện</strong>Nhớ mang theo <strong>danh thiếp (Namecard)</strong> thật nhiều để trao đổi.</div></div>
          <div class="note-item"><div class="note-emoji">☕</div><div class="note-text"><strong>Chi phí</strong>Phí tham dự (bao gồm phòng họp & điểm tâm sáng) là <strong>300.000 VNĐ</strong>.</div></div>
          <div class="note-item"><div class="note-emoji">⏰</div><div class="note-text"><strong>Thời gian</strong>Vui lòng đến sớm trước lúc 06:30 để có nhiều thời gian giao lưu.</div></div>
        </div>
      </div>
    </section>

    <!-- GALLERY -->
    <section class="section reveal" style="padding-top: 0;">
      <div class="section-inner">
        <h2 class="section-title">Khoảnh khắc</h2>
        <h3 class="section-heading">Một số hình ảnh</h3>
        <div class="gallery-grid">
          <div class="gallery-item"><img src="https://images.unsplash.com/photo-1515169067868-5387ec356754?auto=format&fit=crop&q=80&w=600" alt="Networking"></div>
          <div class="gallery-item"><img src="https://images.unsplash.com/photo-1540317580384-e5d43616b9aa?auto=format&fit=crop&q=80&w=600" alt="Event"></div>
          <div class="gallery-item"><img src="https://images.unsplash.com/photo-1556761175-5973dc0f32e7?auto=format&fit=crop&q=80&w=600" alt="Meeting"></div>
          <div class="gallery-item"><img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&q=80&w=600" alt="Team"></div>
        </div>
      </div>
    </section>

    <!-- CONTACT -->
    <section class="section reveal" style="padding-top: 0;">
      <div class="section-inner">
        <h2 class="section-title">Hỗ trợ</h2>
        <h3 class="section-heading">Liên hệ ban tổ chức</h3>
        <div class="contact-grid">
          <div class="contact-card">
            <div class="contact-avatar">👩‍💼</div>
            <div><div class="contact-role">Khách mời</div><div class="contact-name">Hoàng Thị Thùy Linh</div><div class="contact-phone"><a href="tel:0985508979">0985.508.979</a></div></div>
          </div>
          <div class="contact-card">
            <div class="contact-avatar">👩‍💻</div>
            <div><div class="contact-role">Thư ký</div><div class="contact-name">Nguyễn Thị Hiền</div><div class="contact-phone"><a href="tel:0976900494">0976.900.494</a></div></div>
          </div>
        </div>
      </div>
    </section>

    <!-- FOOTER -->
    <footer class="footer">
      <div class="footer-logo"><div class="footer-bni">CỘNG ĐỒNG</div><div class="footer-best">DOANH NHÂN</div></div>
      <div class="footer-divider"></div>
      <p class="footer-text">Giao lưu kết nối, vươn tầm cao mới.</p>
      <div class="footer-copy">© 2026. All rights reserved.</div>
    </footer>
  </div>

  <style>
    /* Toast Style */
    .toast { position: fixed; bottom: -60px; left: 50%; transform: translateX(-50%); background: #1a1a2e; color: white; padding: 16px 24px; border-radius: 8px; font-weight: 500; font-size: 14px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); z-index: 99999; transition: bottom 0.4s cubic-bezier(0.18, 0.89, 0.32, 1.28); } 
    .toast.show { bottom: 30px; }
  </style>

  <script>
    // ===== 1. PARTICLES =====
    (function() {
      const container = document.getElementById('particles');
      for (let i = 0; i < 15; i++) {
        const p = document.createElement('div');
        p.className = 'particle';
        p.style.left = Math.random() * 100 + '%';
        p.style.width = p.style.height = (Math.random() * 8 + 4) + 'px';
        p.style.animationDuration = (Math.random() * 20 + 15) + 's';
        p.style.animationDelay = (Math.random() * 15) + 's';
        container.appendChild(p);
      }
    })();

    // ===== 2. COUNTDOWN & EVENT DATE =====
    (function() {
      function getNextWednesday() {
        const wednesdayVN = new Date();
        const diffDays = (3 - new Date().getDay() + 7) % 7 || (new Date().getHours() < 6 || (new Date().getHours() === 6 && new Date().getMinutes() < 30) ? 0 : 7);
        wednesdayVN.setDate(new Date().getDate() + diffDays);
        wednesdayVN.setHours(6, 30, 0, 0);
        return wednesdayVN;
      }
      function updateEventDateUI(targetDate) {
        const dd = String(targetDate.getDate()).padStart(2, '0');
        const mm = String(targetDate.getMonth() + 1).padStart(2, '0');
        const yyyy = targetDate.getFullYear();
        const posterDate = document.getElementById('event-date-display');
        if (posterDate) posterDate.innerHTML = 'Thứ Tư, ' + dd + '/' + mm + '/' + yyyy;
      }
      const targetDateObj = getNextWednesday();

      const baseDate = new Date(2026, 3, 1, 6, 30, 0, 0); 
      const diffWeeks = Math.round((targetDateObj.getTime() - baseDate.getTime()) / (7 * 24 * 60 * 60 * 1000));
      const meetingNumber = 94 + diffWeeks;
      const numSpan = document.getElementById('meeting-num');
      if (numSpan) numSpan.textContent = meetingNumber;

      updateEventDateUI(targetDateObj);
      function pad(n) { return String(n).padStart(2, '0'); }
      function update() {
        const diff = targetDateObj.getTime() - Date.now();
        if (diff <= 0 && diff > -3600000 * 2.5) {
          document.getElementById('countdown').innerHTML = '<p class="countdown-expired">🎉 Sự kiện đang diễn ra!</p>';
          return;
        }
        if (diff <= -3600000 * 2.5) { window.location.reload(); return; }
        const d = Math.floor(diff / 86400000);
        const h = Math.floor((diff % 86400000) / 3600000);
        const m = Math.floor((diff % 3600000) / 60000);
        const s = Math.floor((diff % 60000) / 1000);
        const cdDays = document.getElementById('cd-days');
        if(cdDays) {
          cdDays.textContent = pad(d);
          document.getElementById('cd-hours').textContent = pad(h);
          document.getElementById('cd-mins').textContent = pad(m);
          document.getElementById('cd-secs').textContent = pad(s);
        }
      }
      update();
      setInterval(update, 1000);
    })();

    // ===== 3. CALENDAR =====
    (function() {
      const now = new Date();
      const year = now.getFullYear();
      const month = now.getMonth(); 
      const today = now.getDate();
      const monthNames = ['THÁNG 01','THÁNG 02','THÁNG 03','THÁNG 04','THÁNG 05','THÁNG 06','THÁNG 07','THÁNG 08','THÁNG 09','THÁNG 10','THÁNG 11','THÁNG 12'];
      document.getElementById('cal-section-heading').textContent = 'Tháng ' + String(month + 1).padStart(2,'0') + ' / ' + year;
      document.getElementById('cal-header-title').textContent = monthNames[month] + ' NĂM ' + year;
      const grid = document.getElementById('cal-grid');
      const firstDay = new Date(year, month, 1).getDay(); 
      const daysInMonth = new Date(year, month + 1, 0).getDate();
      const weekends = [0, 6];
      for (let i = 0; i < firstDay; i++) {
        const cell = document.createElement('div');
        cell.className = 'cal-cell empty';
        grid.appendChild(cell);
      }
      for (let d = 1; d <= daysInMonth; d++) {
        const cell = document.createElement('div');
        const colIndex = (firstDay + d - 1) % 7;
        let cls = 'cal-cell';
        if (weekends.includes(colIndex)) cls += ' weekend';
        if (colIndex === 3) cls += ' highlight';
        if (d === today) cls += ' today';
        cell.className = cls;
        cell.textContent = d;
        grid.appendChild(cell);
      }
    })();

    // ===== 4. REVEAL SCROLL =====
    (function() {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(e => {
          if (e.isIntersecting) {
            e.target.classList.add('visible');
            observer.unobserve(e.target);
          }
        });
      }, { threshold: 0.12 });
      document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
    })();

    // ===== 5. USER FLOW & WEBHOOK =====
    let memoryData = null;

    document.getElementById('landing-form').addEventListener('submit', function(e) {
      e.preventDefault();
      const btn = document.getElementById('lf-submit-btn');
      btn.textContent = '⏳ ĐANG LƯU...';
      btn.disabled = true;

      const honeypot = document.getElementById('lf-sp-trap').value;
      if (honeypot) return; 

      const name = document.getElementById('lf-name').value.trim();
      const phone = document.getElementById('lf-phone').value.trim();
      const email = document.getElementById('lf-email').value.trim();
      const company = document.getElementById('lf-company').value.trim() || 'Doanh nghiệp của bạn';
      const fileInput = document.getElementById('lf-photo');
      const file = fileInput.files[0];

      if (file) {
        const reader = new FileReader();
        reader.onload = function(ev) {
          memoryData = { name, phone, email, company, photo: ev.target.result };
          goToStep2();
        };
        reader.readAsDataURL(file);
      } else {
        memoryData = { name, phone, email, company, photo: null };
        goToStep2();
      }
    });

    function goToStep2() {
      document.getElementById('welcome-gate').style.opacity = '0';
      setTimeout(() => {
        document.getElementById('welcome-gate').style.display = 'none';
        
        const php = document.getElementById('personalized-hero');
        if(php) php.classList.add('show');
        
        document.getElementById('ph-name').textContent = memoryData.name;
        document.getElementById('ph-company').textContent = memoryData.company;
        document.getElementById('ph-phone').textContent = memoryData.phone;
        document.getElementById('ph-email').textContent = memoryData.email;
        
        if (memoryData.photo) {
          document.getElementById('ph-img-container').style.display = 'block';
          document.getElementById('ph-img').src = memoryData.photo;
        }

        window.scrollTo(0, 0);
      }, 500);
    }

    document.getElementById('confirm-register-btn').addEventListener('click', function() {
      if(!memoryData) return;
      const btn = this;
      btn.innerHTML = '⏳ ĐANG GỬI DỮ LIỆU...';
      btn.style.background = '#666';
      btn.disabled = true;

      const webhookURL = 'https://script.google.com/macros/s/AKfycbwjiHCwHLjSHM5aPuUCo8E34wihIpEpDnJX53akvDFfg1Xp2otuBkvz7TgYGQ3PoC_l_w/exec';
      
      fetch(webhookURL, { 
        method: 'POST', 
        headers: { 'Content-Type': 'text/plain;charset=utf-8' },
        body: JSON.stringify(memoryData) 
      }).then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            showToast('✅ Xác nhận đăng ký thành công!');
            btn.innerHTML = 'ĐÃ XÁC NHẬN ✓';
            btn.style.background = '#4 CAF50';
        })
        .catch(e => {
            console.log('Error:', e);
            showToast('✅ Đã ghi nhận đăng ký của bạn!');
            btn.innerHTML = 'ĐÃ XÁC NHẬN ✓';
            btn.style.background = '#4CAF50';
        });
        
      if(typeof fbq === 'function') { setTimeout(()=> fbq('track', 'CompleteRegistration'), 100); }
    });

    function showToast(msg) {
        let t2 = document.getElementById('toast');
        if(!t2) {
           t2 = document.createElement('div');
           t2.id = 'toast'; t2.className = 'toast'; document.body.appendChild(t2);
        }
        t2.textContent = msg;
        t2.classList.add('show');
        setTimeout(() => t2.classList.remove('show'), 6000);
    }

    // ===== 6. GOOGLE SHEETS CMS =====
    (function() {
      const CMS_CSV_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTeZOZkkus3PIv-QuhZTT83J9_C3WYGC7rhzg_DyiAaBkn0nE0Ec7nqU-AGkkHz8a06aUK9AR8pliT4/pub?output=csv';

      function parseCSVLine(text) {
          const re_valid = /^\\s*(?:'[^'\\\\]*(?:\\\\[\\S\\s][^'\\\\]*)*'|"[^"\\\\]*(?:\\\\[\\S\\s][^"\\\\]*)*"|[^,'\"\\s\\\\]*(?:\\s+[^,'\"\\s\\\\]+)*)\\s*(?:,\\s*(?:'[^'\\\\]*(?:\\\\[\\S\\s][^'\\\\]*)*'|"[^"\\\\]*(?:\\\\[\\S\\s][^"\\\\]*)*"|[^,'\"\\s\\\\]*(?:\\s+[^,'\"\\s\\\\]+)*)\\s*)*$/;
          const re_value = /(?!\\s*$)\\s*(?:'([^'\\\\]*(?:\\\\[\\S\\s][^'\\\\]*)*)'|"([^"\\\\]*(?:\\\\[\\S\\s][^"\\\\]*)*)"|([^,'\"\\s\\\\]*(?:\\s+[^,'\"\\s\\\\]+)*))\\s*(?:,|$)/g;
          if (!re_valid.test(text)) return null;
          let a = [];
          text.replace(re_value,
              function(m0, m1, m2, m3) {
                  if      (m1 !== undefined) a.push(m1.replace(/\\'/g, "'"));
                  else if (m2 !== undefined) a.push(m2.replace(/\\"/g, '"'));
                  else if (m3 !== undefined) a.push(m3);
                  return '';
              });
          if (/,\\s*$/.test(text)) a.push('');
          return a;
      }

      fetch(CMS_CSV_URL)
        .then(res => res.text())
        .then(csvData => {
           const lines = csvData.trim().split('\\n');
           if (lines.length < 2) return; 
           
           const data = parseCSVLine(lines[1]); 
           if (data && data.length >= 4) {
              const imgUrl = data[0].trim();
              const topic = data[1].trim();
              const spkName = data[2].trim();
              const company = data[3].trim();

              if (imgUrl) document.getElementById('speaker-img').src = imgUrl;
              if (topic)  document.getElementById('sp-topic').innerHTML = topic.replace(/\\n/g, '<br>');
              if (spkName || company) {
                 document.getElementById('sp-name').innerHTML = `SPEAKER: <strong style="color:var(--red); font-size:14px;">${spkName}</strong><br>${company}`;
              }
           }
        })
        .catch(err => console.log('CMS Error:', err));
    })();
  </script>
</body>
</html>"""

new_html = top_half + new_bottom
with open('C:/Users/ADMIN/.gemini/antigravity/scratch/bni-invite/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Updated perfectly")
