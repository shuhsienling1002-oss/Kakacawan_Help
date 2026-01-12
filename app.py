import streamlit as st

# ==========================================
# 1. 系統設定與 CSS (視覺優化)
# ==========================================
st.set_page_config(
    page_title="膽曼mato'asay福利說明書",
    page_icon="👵",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    /* 全局字體設定 */
    html, body, [class*="css"] {
        font-family: "Microsoft JhengHei", sans-serif;
        font-size: 20px;
        color: #000000;
    }
    
    /* 標題樣式 */
    .main-title {
        font-size: 34px;
        font-weight: 900;
        color: #D32F2F;
        text-align: center;
        margin-bottom: 10px;
    }
    
    /* 福利卡片 (核心顯示區) */
    .benefit-card {
        background-color: #FFFFFF;
        border: 2px solid #333;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 25px;
        box-shadow: 3px 3px 0px #999; /* 復古陰影，增加立體感 */
    }
    
    .card-header {
        font-size: 24px;
        font-weight: 900;
        color: #D32F2F; /* 紅色標題 */
        border-bottom: 2px solid #D32F2F;
        padding-bottom: 10px;
        margin-bottom: 10px;
    }
    
    .money-tag {
        font-size: 28px;
        font-weight: bold;
        color: #1976D2; /* 藍色金額 */
        background-color: #E3F2FD;
        padding: 5px 10px;
        border-radius: 5px;
        display: inline-block;
        margin-bottom: 10px;
    }
    
    /* 步驟區塊 */
    .step-box {
        background-color: #F1F8E9; /* 淺綠底 */
        padding: 15px;
        border-radius: 8px;
        margin-top: 10px;
    }
    .step-title {
        font-weight: bold;
        color: #2E7D32;
        margin-bottom: 5px;
    }
    
    /* 文件清單區塊 */
    .doc-box {
        background-color: #FFF3E0; /* 淺橘底 */
        padding: 15px;
        border-radius: 8px;
        margin-top: 10px;
    }
    .doc-title {
        font-weight: bold;
        color: #E65100;
        margin-bottom: 5px;
    }

    /* 地址電話靜態顯示區 */
    .contact-static {
        margin-top: 15px;
        padding-top: 10px;
        border-top: 1px dashed #999;
        font-size: 18px;
        line-height: 1.6;
    }
    .contact-label {
        background-color: #333;
        color: #fff;
        padding: 2px 6px;
        border-radius: 4px;
        font-size: 16px;
    }

    /* 調整 Tabs */
    button[data-baseweb="tab"] {
        font-size: 20px !important;
        font-weight: bold;
        padding: 10px 5px !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 標題與設定區
# ==========================================
st.markdown('<div class="main-title">膽曼 mato\'asay<br>福利說明書</div>', unsafe_allow_html=True)

with st.expander("📝 點此勾選長輩資料 (必填)", expanded=True):
    age = st.number_input("長輩年齡 (Mihecaan)", 50, 120, 65)
    st.caption("👇 請勾選符合的項目：")
    
    c1, c2 = st.columns(2)
    with c1:
        is_farmer = st.checkbox("有農保 (農民)")
        is_low_income = st.checkbox("中低收入戶")
        has_disability = st.checkbox("有身心障礙手冊")
    with c2:
        is_owner = st.checkbox("名下有房子")
        need_transport = st.checkbox("常去外地看病")
        grandparenting = st.checkbox("幫忙帶孫子")

# ==========================================
# 3. 核心邏輯 (使用 HTML 渲染詳解卡片)
# ==========================================

# 輔助函數：產生詳細卡片 HTML
def render_card(title, money, steps, docs, location, phone, address):
    steps_html = "".join([f"<li>{s}</li>" for s in steps])
    docs_html = "".join([f"<li>{d}</li>" for d in docs])
    
    html = f"""
    <div class="benefit-card">
        <div class="card-header">{title}</div>
        <div class="money-tag">{money}</div>
        
        <div class="step-box">
            <div class="step-title">🚶‍♂️ 申請步驟：</div>
            <ol style="margin-left:-20px; margin-bottom:0;">{steps_html}</ol>
        </div>
        
        <div class="doc-box">
            <div class="doc-title">🎒 準備文件：</div>
            <ul style="margin-left:-20px; margin-bottom:0;">{docs_html}</ul>
        </div>
        
        <div class="contact-static">
            <span class="contact-label">地點</span> <b>{location}</b><br>
            <span class="contact-label">電話</span> <span style="font-size:22px; font-weight:bold; color:#000;">{phone}</span><br>
            <span class="contact-label">地址</span> {address}
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

# 分頁顯示
tabs = st.tabs(["💰領錢", "🩺看病", "🏠房子", "🚌交通", "🆘其他"])

# --- Tab 1: 現金津貼 ---
with tabs[0]:
    if is_farmer and age >= 65:
        render_card(
            title="✅ 老農津貼",
            money="每月 $8,110",
            steps=["確認農保資格滿 15 年。", "帶著證件直接去農會櫃台。", "填寫申請書 (櫃台會幫忙)。"],
            docs=["身分證 (正本)", "印章 (長輩本人的)", "長濱農會存摺 (正本)"],
            location="長濱鄉農會 (保險部)",
            phone="089-832064",
            address="長濱村 9 鄰 63 號"
        )
    elif 55 <= age < 65:
        render_card(
            title="✅ 原住民給付 (國民年金)",
            money="每月 $3,772 起",
            steps=["年滿 55 歲當月即可申請。", "去鄉公所找原民課或村幹事。", "審核通過後，下個月入帳。"],
            docs=["身分證", "印章", "長濱農會或郵局存摺"],
            location="長濱鄉公所 (原民課)",
            phone="089-832139",
            address="長濱村 9 鄰 58 號"
        )
    
    if is_low_income and age >= 65:
        render_card(
            title="✅ 中低收入老人津貼",
            money="$4,164 ~ $8,329",
            steps=["每年年底村幹事會協助調查。", "若新申請，需去公所社會課。", "查調全戶所得與財產。"],
            docs=["全戶戶口名簿", "身分證 + 印章", "郵局存摺"],
            location="長濱鄉公所 (社會課)",
            phone="089-832139",
            address="長濱村 9 鄰 58 號"
        )

    if grandparenting and is_low_income:
        render_card(
            title="👶 弱勢家庭兒童托育補助",
            money="$2,000 ~ $5,000 /月",
            steps=["確認是阿公阿嬤在帶孫子。", "孫子父母無力扶養或單親。", "向公所申請資格認定。"],
            docs=["戶口名簿 (含孫子)", "身分證", "申請表 (去公所拿)"],
            location="長濱鄉公所 (社會課)",
            phone="089-832139",
            address="長濱村 9 鄰 58 號"
        )

# --- Tab 2: 醫療與假牙 ---
with tabs[1]:
    if age >= 55:
        render_card(
            title="🦷 原住民假牙補助",
            money="最高 3萬 ~ 4.4萬",
            steps=[
                "<b>第一步(關鍵)：</b>先帶健保卡去牙醫診所檢查。", 
                "請醫生開立<b>「診斷書」</b>和<b>「估價單」</b>。", 
                "<b>第二步：</b>拿著單子去公所原民課送件。",
                "<b>第三步：</b>收到縣府公文後，再回去診所做假牙。"
            ],
            docs=["身分證", "印章", "健保卡", "診所開的估價單"],
            location="長濱鄉公所 (原民課)",
            phone="089-832139",
            address="長濱村 9 鄰 58 號"
        )

    if need_transport or age >= 55:
        render_card(
            title="🚑 就醫轉診交通費",
            money="實報實銷 (火車/客運)",
            steps=["去衛生所或診所看病。", "醫生開立<b>「轉診單」</b>去外縣市。", "看完病保留<b>「收據」</b>和<b>「車票」</b>。", "回衛生所申請退費。"],
            docs=["轉診單 (粉紅色/綠色)", "醫療收據", "車票票根", "戶口名簿/存摺"],
            location="長濱鄉衛生所",
            phone="089-831022",
            address="長濱村 5 鄰 83 號"
        )
    
    if has_disability:
        render_card(
            title="🦻 身心障礙輔具補助",
            money="視項目 (最高全額)",
            steps=["去慈濟/馬偕做輔具評估。", "拿到評估報告書。", "去公所社會課申請核准。", "購買輔具後請款。"],
            docs=["身心障礙手冊", "評估報告書", "購買發票", "存摺/印章"],
            location="長濱鄉公所 (社會課)",
            phone="089-832139",
            address="長濱村 9 鄰 58 號"
        )

# --- Tab 3: 居住與修繕 ---
with tabs[2]:
    if is_owner:
        render_card(
            title="🔨 住宅修繕補助",
            money="最高 11 萬元",
            steps=[
                "<b>注意時間：</b>每年 1月~3月 開放申請。", 
                "找廠商估價 (如修屋頂、廁所)。", 
                "填寫申請表送公所。",
                "<b>絕對不能先動工！</b>要等核准才能動工。"
            ],
            docs=["建物權狀 (或謄本)", "全戶戶口名簿", "全戶所得證明 (國稅局)", "施工前照片 (洗出來)"],
            location="長濱鄉公所 (原民課)",
            phone="089-832139",
            address="長濱村 9 鄰 58 號"
        )
    else:
        st.info("修繕補助需要房子是自己的。如果是租房，請搜尋「300億租金補貼」。")

# --- Tab 4: 交通 ---
with tabs[3]:
    render_card(
        title="💳 台東卡 (敬老/博愛)",
        money="每月 1500 點",
        steps=["本人親自去公所辦理 (可現場照相)。", "約 2 週後領卡。", "搭火車/客運/愛心計程車時刷卡。"],
        docs=["身分證 (正本)", "2吋照片 2張 (或現場拍)", "印章"],
        location="長濱鄉公所 (社會課)",
        phone="089-832139",
        address="長濱村 9 鄰 58 號"
    )

    st.info("🚕 **TTGO 接送**：這需要上網或電話預約。預約專線：089-220855")

# --- Tab 5: 急難與身後 ---
with tabs[4]:
    if is_farmer:
        render_card(
            title="⚰️ 農保喪葬津貼",
            money="$153,000 (15萬3)",
            steps=["被保險人身故後。", "由支出殯葬費的人申請。", "向農會保險部辦理。"],
            docs=["死亡證明書", "除戶戶籍謄本", "申請人身分證/印章/存摺"],
            location="長濱鄉農會 (保險部)",
            phone="089-832064",
            address="長濱村 9 鄰 63 號"
        )
    
    render_card(
        title="🆘 急難救助",
        money="最高 3 萬元",
        steps=["發生變故 (意外/重病/死亡) 3個月內。", "先找村長證明，或直接去公所。", "社工會訪視評估。"],
        docs=["診斷書 或 死亡證明", "醫療收據", "戶口名簿", "存摺"],
        location="長濱鄉公所 (社會課)",
        phone="089-832139",
        address="長濱村 9 鄰 58 號"
    )

st.markdown("---")
st.caption("長濱鄉福利說明書 v6.0 | 資料來源：台東縣政府/長濱鄉公所")
