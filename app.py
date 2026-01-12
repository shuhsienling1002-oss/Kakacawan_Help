import streamlit as st

# --- 1. 核心設定與樣式 (針對長輩優化) ---
st.set_page_config(
    page_title="膽曼mato'asay福利申請",
    page_icon="👵",
    layout="centered"
)

# CSS 強制放大字體與優化對比
st.markdown("""
    <style>
    /* 全局字體設定：使用微軟正黑體，基礎字級 22px */
    html, body, [class*="css"] {
        font-family: "Microsoft JhengHei", sans-serif;
        font-size: 22px;
    }
    
    /* 標題樣式 (阿美語) */
    .title-text {
        font-size: 38px;
        font-weight: 900;
        color: #B71C1C; /* 部落紅 */
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 1px 1px 2px #ccc;
    }
    
    /* 提示卡片 (黃底黑字) */
    .note-card {
        background-color: #FFF9C4;
        padding: 20px;
        border-radius: 12px;
        border-left: 8px solid #FBC02D;
        margin-bottom: 15px;
    }

    /* 重點福利項目 (綠底) */
    .benefit-box {
        background-color: #E8F5E9;
        padding: 20px;
        border-radius: 12px;
        border: 2px solid #4CAF50;
        margin-bottom: 15px;
    }
    
    /* 警告/注意項目 (紅框) */
    .alert-box {
        border: 3px solid #FF5252;
        padding: 15px;
        border-radius: 10px;
        background-color: #FFEBEE;
    }

    /* 電話卡片 (大字體) */
    .phone-card {
        background-color: #E3F2FD;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 10px;
        border: 2px solid #2196F3;
    }
    .big-phone {
        font-size: 32px;
        font-weight: bold;
        color: #0D47A1;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 標題區 (唯一保留阿美語) ---
st.markdown('<div class="title-text">膽曼 mato\'asay 福利申請</div>', unsafe_allow_html=True)

# --- 3. 側邊欄：身份調查局 (Layer 2 邏輯核心) ---
with st.sidebar:
    st.header("📝 第一步：請勾選資料")
    st.markdown("**(系統會自動幫您算錢)**")
    
    # 年齡輸入
    age = st.number_input("長輩年齡 (Mihecaan)", min_value=50, max_value=120, value=65, step=1)
    
    st.markdown("---")
    st.subheader("長輩的身分是？")
    
    # 關鍵變數
    is_farmer = st.checkbox("有農保 (我是農民)")
    is_low_income = st.checkbox("是中低收入戶")
    has_disability = st.checkbox("有身心障礙手冊")
    is_owner = st.checkbox("名下有房子 (或配偶)")
    need_transport = st.checkbox("常要去玉里/台東看病")

# --- 4. 邏輯運算與顯示 (Layer 1 物理內核) ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["💰 領錢", "🩺 看病", "🏠 房子", "🚌 車子", "🆘 急難"])

# === Tab 1: 現金福利 (智慧排序) ===
with tab1:
    st.subheader("💰 每月津貼")

    # 邏輯 A: 老農津貼 (優先級最高，因為錢最多)
    if is_farmer and age >= 65:
        st.markdown(f"""
        <div class="benefit-box">
            <h3>✅ 老農津貼 (首選！)</h3>
            <p style="font-size:28px; color:#D81B60; font-weight:bold;">每月 $8,110 元</p>
            <p>長輩有農保，領這個最划算！(不能跟國民年金重複領)</p>
            <hr>
            <b>去哪辦：</b>長濱鄉農會 (保險部)<br>
            <b>帶什麼：</b>身分證、印章、農會存摺
        </div>
        """, unsafe_allow_html=True)
    
    # 邏輯 B: 中低收老人 (次高)
    elif is_low_income and age >= 65:
        st.markdown(f"""
        <div class="benefit-box">
            <h3>✅ 中低收入老人津貼</h3>
            <p style="font-size:28px; color:#D81B60; font-weight:bold;">每月 $4,164 ~ $8,329</p>
            <p>依據公所核定的等級發放。</p>
            <hr>
            <b>去哪辦：</b>長濱鄉公所 (社會課)
        </div>
        """, unsafe_allow_html=True)

    # 邏輯 C: 原住民給付 (國民年金)
    elif 55 <= age < 65:
        st.markdown(f"""
        <div class="benefit-box">
            <h3>✅ 原住民給付 (國民年金)</h3>
            <p style="font-size:28px; color:#D81B60; font-weight:bold;">每月 $3,772 起</p>
            <p>55歲就能領！領到65歲再換老人年金。</p>
            <hr>
            <b>去哪辦：</b>長濱鄉公所 (原民課) 或找村里幹事
        </div>
        """, unsafe_allow_html=True)
    
    # 邏輯 D: 一般老人年金
    elif age >= 65:
        st.info("ℹ️ **一般老人年金**：請確認國民年金繳費狀況，每月金額不定。")

    else:
        st.warning("尚未滿 55 歲，目前無固定現金津貼，但可申請急難救助。")

# === Tab 2: 醫療與輔具 ===
with tab2:
    st.subheader("🩺 醫療福利")
    
    # 假牙
    if age >= 55:
        st.markdown("""
        <div class="benefit-box">
            <h3>🦷 原住民假牙補助</h3>
            <p><b>最高補助 3萬 ~ 4萬4千元</b></p>
            <p>一定要「先去牙科檢查拿到估價單」，才能去公所送件！不要順序顛倒喔。</p>
        </div>
        """, unsafe_allow_html=True)
    
    # 健保
    if age >= 55:
        st.success("💳 **健保費全免**：55-64歲原住民，政府幫你繳。")
    
    # 輔具
    st.markdown("---")
    if has_disability:
        st.markdown("""
        <div class="benefit-box">
            <h3>🦻 身障輔具補助</h3>
            <p>助聽器、特製輪椅、電動床。</p>
            <p><b>去哪辦：</b>需去大醫院鑑定 $\\to$ 公所社會課申請。</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("ℹ️ **簡易輔具 (無手冊)**：打 1966 評估，可補助拐杖、便盆椅、一般輪椅。")

# === Tab 3: 居住福利 ===
with tab3:
    st.subheader("🏠 房子福利")
    
    if is_owner:
        st.markdown("""
        <div class="alert-box">
            <h3>🔨 修繕住宅 (搶手！)</h3>
            <p><b>最高補助 11 萬元</b> (修屋頂、廁所、廚房)</p>
            <p><b>⚠️ 注意：</b>每年 1月~3月 開放申請，額滿就沒了！</p>
            <hr>
            <b>必備文件檢查：</b>
        </div>
        """, unsafe_allow_html=True)
        c1 = st.checkbox("1. 戶口名簿影本")
        c2 = st.checkbox("2. 建物權狀 (或謄本)")
        c3 = st.checkbox("3. 國稅局所得證明")
        c4 = st.checkbox("4. 施工前照片")
        
        if c1 and c2 and c3 and c4:
            st.balloons()
            st.success("資料齊全！快去公所原民課！")
    else:
        st.warning("申請修繕補助，房子必須是本人或配偶的喔。")
        st.info("💡 **租屋補貼**：如果是租房，可申請內政部300億租金補貼。")

# === Tab 4: 交通福利 (長濱特供) ===
with tab4:
    st.subheader("🚌 出門福利")

    # 轉診交通費 (隱藏版)
    if need_transport or age >= 55:
        st.markdown("""
        <div class="benefit-box">
            <h3>🚑 轉診交通費 (長濱人必看)</h3>
            <p>醫生開轉診單去外縣市(花蓮/台東)看病，車錢可以退！</p>
            <p><b>補助：</b>火車/客運費 實報實銷 (一年最高3萬)</p>
            <p><b>去哪辦：</b>長濱衛生所</p>
        </div>
        """, unsafe_allow_html=True)

    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.info("💳 **台東卡 (敬老)**\n\n每月1500點，搭車免費。")
    with col_t2:
        st.info("🚕 **TTGO 接送**\n\n長濱-玉里/台東 共乘預約。")

# === Tab 5: 急難與法律 ===
with tab5:
    st.subheader("🆘 救命專區")
    
    st.write("發生意外、喪葬、或嚴重車禍糾紛時使用。")
    
    st.markdown("""
    <div class="note-card">
        <h4>1. 急難救助 (最高3萬)</h4>
        <p>家裡發生變故 3個月內，找村長或公所申請。</p>
    </div>
    <div class="note-card">
        <h4>2. 原住民法律扶助</h4>
        <p>如果你是被告或要告人，律師費政府出。</p>
        <p><b>電話：</b>02-2507-8659 (法扶原民專線)</p>
    </div>
    """, unsafe_allow_html=True)

# --- 5. 底部：超大通訊錄 ---
st.markdown("---")
st.header("📞 聯絡電話簿")

c1, c2 = st.columns(2)

with c1:
    st.markdown("""
    <div class="phone-card">
        長濱鄉公所 (原民/社會課)
        <span class="big-phone">089-832139</span>
        <div style="font-size:18px; margin-top:5px;">長濱村9鄰58號</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="phone-card">
        長濱鄉農會 (保險部)
        <span class="big-phone">089-832064</span>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="phone-card">
        長照服務專線 (找看護)
        <span class="big-phone">1966</span>
        <div style="font-size:18px; margin-top:5px;">手機直接撥打</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="phone-card">
        長濱衛生所 (看牙/轉診)
        <span class="big-phone">089-831022</span>
    </div>
    """, unsafe_allow_html=True)
