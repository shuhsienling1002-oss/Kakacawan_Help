import streamlit as st

# ==========================================
# 1. 系統設定與 CSS 優化 (手機友善版)
# ==========================================
st.set_page_config(
    page_title="膽曼mato'asay福利全書",
    page_icon="👵",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 強制 CSS：字體特大、按鈕好按、手機版面優化
st.markdown("""
    <style>
    /* 全局字體 */
    html, body, [class*="css"] {
        font-family: "Microsoft JhengHei", sans-serif;
        font-size: 20px;
    }
    
    /* 標題優化 */
    .main-title {
        font-size: 34px;
        font-weight: 900;
        color: #B71C1C; /* 阿美紅 */
        text-align: center;
        margin-bottom: 5px;
        text-shadow: 1px 1px 2px #ddd;
    }
    .sub-title {
        font-size: 18px;
        color: #555;
        text-align: center;
        margin-bottom: 20px;
    }

    /* 福利卡片設計 (重要！) */
    .benefit-card {
        background-color: #fff;
        border: 2px solid #4CAF50;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    .benefit-title {
        font-size: 24px;
        font-weight: bold;
        color: #2E7D32;
        margin-bottom: 5px;
    }
    .benefit-money {
        font-size: 28px;
        font-weight: bold;
        color: #D81B60;
        display: block;
        margin-bottom: 10px;
    }
    .benefit-tag {
        background-color: #E8F5E9;
        color: #2E7D32;
        padding: 3px 8px;
        border-radius: 5px;
        font-size: 16px;
        font-weight: bold;
    }
    
    /* 警示與重要資訊 */
    .alert-box {
        background-color: #FFEBEE;
        border: 2px solid #D32F2F;
        padding: 10px;
        border-radius: 8px;
        margin-top: 10px;
    }
    
    /* 電話按鈕優化 */
    .phone-btn {
        display: block;
        width: 100%;
        background-color: #E3F2FD;
        color: #0D47A1;
        text-align: center;
        padding: 15px;
        margin: 5px 0;
        border-radius: 10px;
        text-decoration: none;
        font-weight: bold;
        font-size: 22px;
        border: 2px solid #2196F3;
    }
    
    /* 調整 Tabs 點擊區 */
    button[data-baseweb="tab"] {
        font-size: 18px !important; 
        font-weight: bold;
        padding: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 標題與輸入區 (手機置頂摺疊設計)
# ==========================================
st.markdown('<div class="main-title">膽曼 mato\'asay<br>福利全書</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">收錄長濱鄉最完整的原住民長者權益</div>', unsafe_allow_html=True)

# 使用 Expander 讓手機畫面不雜亂
with st.expander("📝 設定長輩資料 (勾選越多，福利越多)", expanded=True):
    # 年齡輸入
    age = st.number_input("長輩年齡 (Mihecaan)", 50, 120, 65)
    
    st.markdown("---")
    st.caption("👇 請詳細勾選 (這些都會影響福利！)")
    
    # 基礎身份
    col1, col2 = st.columns(2)
    with col1:
        is_farmer = st.checkbox("有農保 (農民)")
        is_low_income = st.checkbox("中低收入戶")
        has_disability = st.checkbox("身心障礙手冊")
    with col2:
        is_owner = st.checkbox("名下有房子")
        need_transport = st.checkbox("常去外地看病")
        grandparenting = st.checkbox("正在幫忙帶孫子") # 隔代教養

    # 進階身份 (隱藏版福利)
    st.markdown("---")
    st.caption("👇 進階狀況 (如果有)")
    has_car = st.checkbox("名下有車子 (牌照稅減免)")
    live_in_institution = st.checkbox("住在安養機構")
    
# ==========================================
# 3. 核心邏輯運算與顯示
# ==========================================

# 定義 Tabs (分類更細)
tabs = st.tabs(["💰領錢", "🩺醫療", "🏠居住", "👶照顧", "⚰️身後"])

# --- Tab 1: 現金津貼 (月領類) ---
with tabs[0]:
    st.info("💡 這是每個月可以領的生活費")
    
    # 邏輯：老農 vs 國民年金 (互斥)
    if is_farmer and age >= 65:
        st.markdown(f"""
        <div class="benefit-card">
            <div class="benefit-title">✅ 老農津貼</div>
            <span class="benefit-money">$8,110 /月</span>
            <p>農保滿15年可全領。這是長濱長輩最穩定的收入。</p>
            <hr>
            <b>去哪辦：</b>長濱鄉農會 保險部
        </div>
        """, unsafe_allow_html=True)
    elif 55 <= age < 65:
        st.markdown(f"""
        <div class="benefit-card">
            <div class="benefit-title">✅ 原住民給付 (國民年金)</div>
            <span class="benefit-money">$3,772 起 /月</span>
            <p>55歲就能領！不用等到65歲。</p>
            <hr>
            <b>去哪辦：</b>長濱鄉公所 原民課
        </div>
        """, unsafe_allow_html=True)
    elif age >= 65 and not is_farmer:
        st.markdown(f"""
        <div class="benefit-card">
            <div class="benefit-title">✅ 老人年金 (國民年金)</div>
            <span class="benefit-money">視投保年資而定</span>
            <p>若有欠費，請諮詢公所分期繳納後領取。</p>
        </div>
        """, unsafe_allow_html=True)

    # 邏輯：中低收入 (可疊加)
    if is_low_income and age >= 65:
        st.markdown(f"""
        <div class="benefit-card">
            <div class="benefit-title">✅ 中低收入老人生活津貼</div>
            <span class="benefit-money">$4,164 ~ $8,329 /月</span>
            <p>依據家庭收入審核等級。</p>
            <hr>
            <b>去哪辦：</b>長濱鄉公所 社會課
        </div>
        """, unsafe_allow_html=True)

    # 邏輯：隔代教養 (隱藏版！)
    if grandparenting and is_low_income:
         st.markdown(f"""
        <div class="benefit-card">
            <div class="benefit-title">👶 弱勢家庭兒童托育補助</div>
            <span class="benefit-money">$2,000 ~ $5,000 /月</span>
            <p>如果是阿公阿嬤幫忙帶孫子(且符合弱勢資格)，可以申請！</p>
            <hr>
            <b>去哪辦：</b>長濱鄉公所 社會課
        </div>
        """, unsafe_allow_html=True)

# --- Tab 2: 醫療與輔具 (包含稅務) ---
with tabs[1]:
    st.info("💡 看醫生、裝牙齒、買輪椅")
    
    # 假牙
    if age >= 55:
        st.markdown("""
        <div class="benefit-card">
            <div class="benefit-title">🦷 原住民假牙補助</div>
            <span class="benefit-money">最高 3萬 ~ 4.4萬</span>
            <div class="alert-box">⚠️ 程序：先去牙醫診所拿「估價單」 $\\to$ 再去公所送件！</div>
        </div>
        """, unsafe_allow_html=True)

    # 健保費
    if age >= 55:
        st.markdown("""
        <div class="benefit-card">
            <div class="benefit-title">💳 健保費全額補助</div>
            <span class="benefit-money">政府幫你繳</span>
            <p>55-64歲原住民，健保局自動處理。</p>
        </div>
        """, unsafe_allow_html=True)
        
    # 轉診交通費
    if need_transport or age >= 55:
        st.markdown("""
        <div class="benefit-card">
            <div class="benefit-title">🚑 原住民就醫轉診交通費</div>
            <span class="benefit-money">實報實銷 (一年3萬)</span>
            <p>長濱沒大醫院，醫生開轉診單去台東/花蓮，<b>車錢可以退！</b></p>
            <hr>
            <b>去哪辦：</b>長濱衛生所
        </div>
        """, unsafe_allow_html=True)

    # 輔具
    if has_disability:
        st.markdown("""
        <div class="benefit-card">
            <div class="benefit-title">🦻 身心障礙輔具</div>
            <span class="benefit-money">最高全額補助</span>
            <p>助聽器、特製機車、電動床、氣墊床。</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="benefit-card">
            <div class="benefit-title">🦯 長照簡易輔具</div>
            <span class="benefit-money">補助 70% ~ 100%</span>
            <p>一般老人也可申請：拐杖、便盆椅、一般輪椅。</p>
            <b>方法：</b>手機撥打 1966
        </div>
        """, unsafe_allow_html=True)

# --- Tab 3: 居住與稅務 (包含修繕、租金、免稅) ---
with tabs[2]:
    st.info("💡 住得安全、省稅金")

    if is_owner:
        st.markdown("""
        <div class="benefit-card">
            <div class="benefit-title">🔨 住宅修繕補助</div>
            <span class="benefit-money">最高 11 萬元</span>
            <p>修屋頂、廁所、廚房。<b>每年1-3月搶先申請！</b></p>
        </div>
        <div class="benefit-card">
            <div class="benefit-title">🏠 建購住宅補助</div>
            <span class="benefit-money">最高 22 萬元</span>
            <p>蓋房子或買房子。</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="benefit-card">
            <div class="benefit-title">🏠 租金補貼 (300億專案)</div>
            <span class="benefit-money">每月補貼租金</span>
            <p>如果房子是用租的，可以申請。</p>
        </div>
        """, unsafe_allow_html=True)
        
    # 隱藏版：牌照稅減免
    if has_disability and has_car:
        st.markdown("""
        <div class="benefit-card">
            <div class="benefit-title">🚗 使用牌照稅減免</div>
            <span class="benefit-money">免稅 (最高11,230元)</span>
            <p>身心障礙者(或載送他的家人)的車子，可以免繳牌照稅！</p>
            <hr>
            <b>去哪辦：</b>台東縣稅務局 (可請公所代轉)
        </div>
        """, unsafe_allow_html=True)

# --- Tab 4: 照顧與生活 (長照、文健站) ---
with tabs[3]:
    st.info("💡 有人顧、有飯吃")
    
    st.markdown("""
    <div class="benefit-card">
        <div class="benefit-title">🚌 台東卡 (愛心/敬老)</div>
        <span class="benefit-money">每月 1500 點</span>
        <p>搭公車免費，也可抵扣「愛心計程車」車資。</p>
    </div>
    
    <div class="benefit-card">
        <div class="benefit-title">🥗 部落文健站 (C據點)</div>
        <span class="benefit-money">免費供餐/活動</span>
        <p>膽曼就有文健站！白天去那邊運動、聊天、吃午餐。</p>
    </div>
    
    <div class="benefit-card">
        <div class="benefit-title">🚕 TTGO 預約接送</div>
        <span class="benefit-money">共乘優惠價</span>
        <p>長濱-玉里 / 長濱-台東市。解決長濱沒車的問題。</p>
    </div>
    """, unsafe_allow_html=True)

    if live_in_institution:
         st.markdown("""
        <div class="benefit-card">
            <div class="benefit-title">🏨 住宿式機構補助</div>
            <span class="benefit-money">每年最高 12 萬元</span>
            <p>如果長輩住在安養中心，政府會補貼費用。</p>
        </div>
        """, unsafe_allow_html=True)

# --- Tab 5: 身後與急難 (這部分最常被忽略) ---
with tabs[4]:
    st.warning("⚠️ 備而不用，但權益巨大")

    if is_farmer:
        st.markdown("""
        <div class="benefit-card">
            <div class="benefit-title">⚰️ 農保喪葬津貼</div>
            <span class="benefit-money">$153,000 元 (15萬3)</span>
            <p><b>這筆錢非常多！</b>農民身故後，家屬一定要去農會申請。</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="benefit-card">
            <div class="benefit-title">⚰️ 國保喪葬給付</div>
            <span class="benefit-money">約 $98,805 元</span>
            <p>如果是領國民年金者身故，家屬可領取 5 個月的喪葬給付。</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="benefit-card">
        <div class="benefit-title">🆘 急難救助 (鄉/縣/中央)</div>
        <span class="benefit-money">$10,000 ~ $30,000</span>
        <p>發生意外、喪葬無力支付時。請先找村長或公所。</p>
    </div>
    
    <div class="benefit-card">
        <div class="benefit-title">⚖️ 原住民法律扶助</div>
        <span class="benefit-money">律師費全免</span>
        <p>遇到官司糾紛，不要怕沒錢請律師。法扶基金會全額補助。</p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# 4. 底部通訊錄 (可直接撥打)
# ==========================================
st.markdown("---")
st.markdown("<h3 style='text-align:center;'>📞 點擊下方直接撥打</h3>", unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    st.markdown('<a href="tel:089832139" class="phone-btn">🏛️ 公所原民課<br><span style="font-size:16px">(福利申請)</span></a>', unsafe_allow_html=True)
    st.markdown('<a href="tel:089832064" class="phone-btn">🌾 長濱農會<br><span style="font-size:16px">(老農津貼)</span></a>', unsafe_allow_html=True)
with c2:
    st.markdown('<a href="tel:1966" class="phone-btn">👩‍🦽 1966長照<br><span style="font-size:16px">(找看護/輔具)</span></a>', unsafe_allow_html=True)
    st.markdown('<a href="tel:089831022" class="phone-btn">🏥 長濱衛生所<br><span style="font-size:16px">(看牙/轉診)</span></a>', unsafe_allow_html=True)
