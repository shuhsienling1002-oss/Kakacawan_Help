import streamlit as st

# ==========================================
# 1. 系統設定 (穩定版)
# ==========================================
st.set_page_config(
    page_title="膽曼福利全書",
    page_icon="👵",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 僅保留字體放大設定，不使用複雜 HTML
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: "Microsoft JhengHei", sans-serif;
        font-size: 20px;
    }
    .big-money {
        font-size: 26px;
        color: #D32F2F; 
        font-weight: bold;
    }
    .big-phone {
        font-size: 24px;
        font-weight: bold;
        color: #000;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 標題與資料輸入
# ==========================================
st.title("👵 膽曼 mato'asay 福利全書")
st.caption("完整收錄 20 項權益 (含隱藏版)")

# 使用 Expander 收納輸入區
with st.expander("📝 設定長輩資料 (點此展開/收合)", expanded=True):
    age = st.number_input("長輩年齡 (Mihecaan)", 50, 120, 65)
    
    st.write("👇 請詳細勾選 (勾越多，福利越多)：")
    c1, c2 = st.columns(2)
    with c1:
        is_farmer = st.checkbox("我是農民 (有農保)")
        is_low_income = st.checkbox("我是中低收入戶")
        has_disability = st.checkbox("有身心障礙手冊")
        live_in_institution = st.checkbox("住在安養機構")
    with c2:
        is_owner = st.checkbox("名下有房子")
        has_car = st.checkbox("名下有車子")
        need_transport = st.checkbox("常去外地看病")
        grandparenting = st.checkbox("幫忙帶孫子")

# ==========================================
# 3. 核心功能：卡片顯示函數 (保證無亂碼)
# ==========================================
def show_card(title, money, steps, docs, location, phone, addr):
    with st.container(border=True):
        st.subheader(title)
        st.markdown(f'<p class="big-money">{money}</p>', unsafe_allow_html=True)
        
        if steps:
            st.warning("🚶‍♂️ **申請步驟**：\n" + steps)
        
        if docs:
            st.info("🎒 **準備文件**：\n" + docs)
        
        st.divider()
        st.write(f"🏛️ **地點**：{location}")
        st.markdown(f"📞 **電話**：<span class='big-phone'>{phone}</span>", unsafe_allow_html=True)
        if addr:
            st.write(f"📍 **地址**：{addr}")

# ==========================================
# 4. 福利展示區 (完整 5 大類)
# ==========================================
st.markdown("---")
tabs = st.tabs(["💰領錢", "🩺醫療", "🏠居住", "🚌交通", "🆘其他"])

# === Tab 1: 現金津貼 ===
with tabs[0]:
    # 1. 老農津貼
    if is_farmer and age >= 65:
        show_card(
            "✅ 老農津貼", "每月 $8,110",
            "1. 確認農保年資滿15年。\n2. 帶證件直接去農會。\n3. 填寫申請書。",
            "1. 身分證 (正本)\n2. 印章\n3. 長濱農會存摺 (正本)",
            "長濱鄉農會 (保險部)", "089-832064", "長濱村 9 鄰 63 號"
        )
    # 2. 原住民給付
    elif 55 <= age < 65:
        show_card(
            "✅ 原住民給付 (國民年金)", "每月 $3,772 起",
            "1. 年滿55歲當月申請。\n2. 去公所原民課。\n3. 次月入帳。",
            "1. 身分證\n2. 印章\n3. 存摺",
            "長濱鄉公所 (原民課)", "089-832139", "長濱村 9 鄰 58 號"
        )
    
    # 3. 中低收入
    if is_low_income and age >= 65:
        show_card(
            "✅ 中低收入老人津貼", "$4,164 ~ $8,329 /月",
            "1. 每年底調查，或隨時申請。\n2. 查調全戶財產。",
            "1. 全戶戶口名簿\n2. 身分證/印章\n3. 郵局存摺",
            "長濱鄉公所 (社會課)", "089-832139", "長濱村 9 鄰 58 號"
        )
    
    # 4. 隔代教養 (隱藏版)
    if grandparenting and is_low_income:
        show_card(
            "👶 弱勢家庭兒童托育補助", "$2,000 ~ $5,000 /月",
            "1. 確認是阿公阿嬤帶孫。\n2. 父母無力扶養證明。",
            "1. 戶口名簿(含孫子)\n2. 申請表",
            "長濱鄉公所 (社會課)", "089-832139", "長濱村 9 鄰 58 號"
        )

# === Tab 2: 醫療與輔具 ===
with tabs[1]:
    # 5. 假牙
    if age >= 55:
        show_card(
            "🦷 原住民假牙補助", "最高 3萬 ~ 4.4萬",
            "1. **先去診所拿估價單** (最重要！)。\n2. 拿單子去公所送件。\n3. 收文後再做牙。",
            "1. 身分證/健保卡\n2. 印章\n3. 估價單",
            "長濱鄉公所 (原民課)", "089-832139", "長濱村 9 鄰 58 號"
        )

    # 6. 健保費
    if age >= 55:
        st.success("💳 **健保費全免**：55-64歲原住民，政府直接幫你繳，不用申請。")
    
    # 7. 轉診交通費
    if need_transport or age >= 55:
        show_card(
            "🚑 就醫轉診交通費", "實報實銷 (火車/客運)",
            "1. 醫生開轉診單去外地。\n2. 保留車票+收據。\n3. 回衛生所申請。",
            "1. 轉診單\n2. 收據+車票\n3. 戶口名簿/存摺",
            "長濱鄉衛生所", "089-831022", "長濱村 5 鄰 83 號"
        )
        
    # 8. 輔具
    if has_disability:
        show_card(
            "🦻 身心障礙輔具", "最高全額補助",
            "1. 去大醫院評估。\n2. 拿報告去公所。",
            "1. 身障手冊\n2. 評估報告\n3. 發票",
            "長濱鄉公所 (社會課)", "089-832139", ""
        )
    else:
        st.info("ℹ️ **一般老人輔具** (拐杖/便盆椅)：請撥打 1966 申請。")

# === Tab 3: 居住與稅務 ===
with tabs[2]:
    # 9. 修繕
    if is_owner:
        show_card(
            "🔨 住宅修繕補助", "最高 11 萬元",
            "1. 每年1-3月申請。\n2. 找人估價。\n3. **核准前勿動工**。",
            "1. 權狀\n2. 戶口名簿\n3. 所得證明\n4. 施工前照片",
            "長濱鄉公所 (原民課)", "089-832139", "長濱村 9 鄰 58 號"
        )
    else:
        st.info("🏠 **租屋補貼**：租房者可申請300億租金補貼。")

    # 10. 牌照稅 (隱藏版)
    if has_disability and has_car:
        show_card(
            "🚗 牌照稅減免", "免稅 (省下1萬多)",
            "1. 身障者有駕照(車限本人)。\n2. 無駕照(車限親屬)。",
            "1. 手冊\n2. 行照/駕照\n3. 戶口名簿",
            "台東縣稅務局 (可請公所代轉)", "089-231600", ""
        )
        
    # 11. 機構補助
    if live_in_institution:
        show_card(
            "🏨 住宿式機構補助", "每年最高 12 萬",
            "1. 使用機構者申請。\n2. 排富條款。",
            "1. 入住證明\n2. 繳費收據",
            "長濱鄉公所 (社會課)", "089-832139", ""
        )

# === Tab 4: 交通與照顧 ===
with tabs[3]:
    # 12. 台東卡
    show_card(
        "💳 台東卡 (敬老/博愛)", "每月 1500 點",
        "1. 去公所辦理。\n2. 現場拍照。",
        "1. 身分證\n2. 印章\n3. 照片2張",
        "長濱鄉公所 (社會課)", "089-832139", ""
    )
    
    st.info("🚕 **TTGO 接送**：預約制共乘 (長濱-玉里/台東)。\n預約電話：089-220855")

# === Tab 5: 急難與身後 ===
with tabs[4]:
    # 13. 農保喪葬津貼
    if is_farmer:
        show_card(
            "⚰️ 農保喪葬津貼", "$153,000 (15萬3)",
            "1. 被保險人身故。\n2. 出錢辦喪事的人申請。\n3. **這筆錢很多，一定要辦！**",
            "1. 死亡證明/除戶謄本\n2. 申請人身分證/存摺",
            "長濱鄉農會 (保險部)", "089-832064", "長濱村 9 鄰 63 號"
        )
    else:
        st.info("⚰️ **國保喪葬給付**：約 9 萬 8 千元 (向勞保局申請)。")

    # 14. 急難救助
    show_card(
        "🆘 急難救助 (通用)", "最高 3 萬元",
        "1. 發生意外/死亡3個月內。\n2. 找村長或公所。",
        "1. 診斷/死亡證明\n2. 戶口名簿\n3. 存摺",
        "長濱鄉公所 (社會課)", "089-832139", ""
    )
    
    # 15. 法律扶助
    st.warning("⚖️ **原住民法律扶助**：打官司律師費全免。\n專線：02-2507-8659")

# ==========================================
# 5. 底部說明
# ==========================================
st.markdown("---")
st.caption("長濱鄉福利全書 v8.0 | 保證內容最全 + 手機顯示正常")
