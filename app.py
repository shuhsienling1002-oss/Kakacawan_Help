import streamlit as st

# --- 1. 頁面設定與 CSS 優化 (老人友善介面) ---
st.set_page_config(
    page_title="膽曼mato'asay福利申請",
    page_icon="👵",
    layout="centered"
)

# 自定義 CSS：加大字體、優化按鈕、增加對比度
st.markdown("""
    <style>
    /* 全局字體加大 */
    html, body, [class*="css"] {
        font-family: "Microsoft JhengHei", sans-serif;
        font-size: 20px;
    }
    
    /* 標題樣式 */
    .title-text {
        font-size: 32px;
        font-weight: bold;
        color: #8B0000; /* 深紅色 */
        text-align: center;
        padding-bottom: 20px;
    }
    
    /* 檢查清單樣式加強 */
    .stCheckbox label {
        font-size: 22px !important;
        font-weight: bold;
        color: #333;
    }
    
    /* 資訊卡片 */
    .info-card {
        padding: 15px;
        background-color: #f0f2f6;
        border-radius: 10px;
        margin-bottom: 15px;
        border-left: 6px solid #8B0000;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 標題區 (唯一保留阿美語) ---
st.markdown('<div class="title-text">膽曼 mato\'asay 福利申請</div>', unsafe_allow_html=True)

# --- 3. 側邊欄：輸入資料 ---
with st.sidebar:
    st.header("📝 第一步：輸入資料")
    
    # 年齡滑桿
    age = st.number_input("請問長輩今年幾歲？", min_value=50, max_value=120, value=60, step=1)
    
    # 資格勾選
    st.markdown("---")
    st.subheader("特殊身分")
    has_disability = st.checkbox("領有身心障礙手冊")
    is_owner = st.checkbox("房子是長輩名下的 (或配偶)")

# --- 4. 主功能區 ---
tab1, tab2, tab3, tab4 = st.tabs(["💰 領錢津貼", "🦷 假牙/醫療", "🏠 房屋修繕", "🚌 交通/照顧"])

# --- Tab 1: 現金津貼 ---
with tab1:
    st.subheader("💰 現金與津貼")
    
    # 邏輯判斷
    if 55 <= age < 65:
        st.success(f"✅ 符合資格：原住民給付 (國民年金)")
        st.info("💡 每個月可領：約 $3,772 ~ $4,049 元")
        
        st.markdown('<div class="info-card">👇 申請前請準備 (請打勾確認)：</div>', unsafe_allow_html=True)
        st.checkbox("1. 長輩的身分證 (正本)")
        st.checkbox("2. 長濱農會存摺 (或郵局)")
        st.checkbox("3. 印章")
        
        st.markdown("---")
        st.markdown("**辦理地點：長濱鄉公所**")
        st.link_button("📍 查看公所地圖位置", "https://www.google.com/maps/search/?api=1&query=台東縣長濱鄉公所")

    elif age >= 65:
        st.success(f"✅ 符合資格：老人年金 (或老農津貼)")
        st.write("已滿 65 歲，轉領一般老人年金。")
        
        st.markdown('<div class="info-card">👇 申請前請準備：</div>', unsafe_allow_html=True)
        st.checkbox("1. 身分證")
        st.checkbox("2. 存摺")
        st.checkbox("3. 印章")
        
        st.markdown("---")
        st.markdown("**辦理地點：長濱鄉公所**")
        st.link_button("📍 查看公所地圖位置", "https://www.google.com/maps/search/?api=1&query=台東縣長濱鄉公所")
    
    else:
        st.warning("🚑 急難救助 (發生意外/生病/喪葬)")
        st.write("若家裡發生變故，3個月內隨時可去公所申請。")
        st.checkbox("診斷證明書 或 收據")
        st.checkbox("戶口名簿")

# --- Tab 2: 醫療與假牙 ---
with tab2:
    st.subheader("🦷 假牙與醫療")
    
    if age >= 55:
        st.success("✅ 符合資格：原住民假牙補助")
        st.write("最高補助 $30,000 ~ $44,000")
        
        st.markdown('<div class="info-card">👇 申請步驟與資料 (照著做)：</div>', unsafe_allow_html=True)
        step1 = st.checkbox("第一步：帶健保卡，去牙科拿「估價單」")
        step2 = st.checkbox("第二步：帶身分證、印章、估價單")
        step3 = st.checkbox("第三步：去公所原民課送件")
        
        if step1 and step2 and step3:
            st.balloons()
            st.success("太棒了！資料都齊全了，快去公所吧！")
            
        st.markdown("---")
        col_map1, col_map2 = st.columns(2)
        with col_map1:
             st.markdown("**看牙齒 (衛生所)**")
             st.link_button("📍 查看衛生所地圖", "https://www.google.com/maps/search/?api=1&query=台東縣長濱鄉衛生所")
        with col_map2:
             st.markdown("**送件 (公所)**")
             st.link_button("📍 查看公所地圖", "https://www.google.com/maps/search/?api=1&query=台東縣長濱鄉公所")

    else:
        st.info("假牙補助需滿 55 歲。")
    
    st.markdown("---")
    st.subheader("🦻 助聽器/輔具")
    if has_disability:
        st.success("有身障手冊：請去大醫院鑑定後，找公所社會課申請。")
    else:
        st.write("無手冊：請撥打 **1966** 申請簡易輔具 (拐杖/輪椅)。")

# --- Tab 3: 房屋修繕 ---
with tab3:
    st.subheader("🏠 房屋修繕/建購")
    
    if is_owner:
        st.success("✅ 資格初判符合 (屋主)")
        st.write("修繕最高 11 萬 / 建購最高 22 萬")
        st.error("⚠️ 注意：每年 1-3 月要趕快去排隊！")
        
        st.markdown('<div class="info-card">👇 必備文件清單 (缺一不可)：</div>', unsafe_allow_html=True)
        st.checkbox("1. 全戶戶口名簿 (影本)")
        st.checkbox("2. 建物權狀 (或謄本)")
        st.checkbox("3. 全戶所得證明 (國稅局申請)")
        st.checkbox("4. 施工前照片 (要洗出來)")
        
        st.markdown("---")
        st.markdown("**辦理地點：長濱鄉公所 (原民課)**")
        st.link_button("📍 查看公所地圖位置", "https://www.google.com/maps/search/?api=1&query=台東縣長濱鄉公所")
    else:
        st.error("❌ 資格不符：房子必須是本人或配偶的喔。")

# --- Tab 4: 交通與照顧 ---
with tab4:
    st.subheader("🚌 出門與照顧")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("🚍 台東卡 (敬老)")
        st.write("搭車免費/愛心計程車")
        st.checkbox("大頭照 3 張")
        st.checkbox("身分證 + 印章")
    with col2:
        st.info("🚗 TTGO 接送")
        st.write("去玉里/台東市共乘")
        st.write("預約制")

    st.markdown("---")
    st.markdown("### 📞 常用電話 (點擊撥打)")
    st.write("長濱鄉公所：089-832139")
    st.write("長照專線：1966")