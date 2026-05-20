import os
from datetime import date
import streamlit as st

st.set_page_config(
    page_title="本格派・日干タイプ診断",
    layout="centered"
)

# UIカスタマイズ：パステルカラーの背景、和モダンで洗練されたカードデザイン、ボタン調整
# スマホでも選択肢（1〜5の数字など）が潰れず、快適にタップできるように横幅と余白を最適化しました。
st.markdown("""
<style>
/* 全体背景：東洋の自然哲学を感じさせる、温かみのある生成り色 */
.stApp {
    background: linear-gradient(135deg, #FAF7F2 0%, #FFFDF9 100%);
}

h1, h2, h3 {
    text-align: center;
    color: #3E2723;
    font-family: 'Helvetica Neue', Arial, 'Hiragino Kaku Gothic ProN', 'BIZ UDPGothic', sans-serif;
}

/* 計算ボタンをスマートかつ上質に */
.stButton>button {
    width: 100%;
    height: 60px;
    font-size: 20px;
    font-weight: bold;
    border-radius: 12px;
    background: linear-gradient(90deg, #D4A373 0%, #CCD5AE 100%);
    color: white;
    border: none;
    box-shadow: 0 4px 12px rgba(212, 163, 115, 0.3);
    transition: all 0.3s ease;
}

.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(212, 163, 115, 0.5);
    color: #FFF;
}

/* 【スマホ最適化】横幅が狭くならないよう、100%に広げて余白を調整 */
.block-container {
    max-width: 100% !important;
    width: 100%;
    margin: auto;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
    padding-top: 3rem !important;
    padding-bottom: 3rem !important;
}

/* パソコンで見るときだけ、中央に程よい幅で表示させる */
@media (min-width: 576px) {
    .block-container {
        max-width: 480px !important;
    }
}

/* 結果表示カードのスタイリング（和の風合いとエレガントさの融合） */
.result-card {
    background: white;
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0 8px 24px rgba(62, 39, 35, 0.05);
    border: 1px solid #EFEAE2;
    text-align: center;
    margin-top: 25px;
}
</style>
""", unsafe_allow_html=True)

# 渾天儀のバナー画像（画像ファイルがない場合でもエラーにせず、美しい文字タイトルを表示する安全設計）
image_filename = "18255025033873457806.jpeg"
if os.path.exists(image_filename):
    try:
        st.image(image_filename, use_container_width=True)
    except Exception:
        # 万が一読み込みエラーが起きた場合の安全策
        st.markdown("<h1 style='color: #D4A373; font-size: 28px; letter-spacing: 2px; margin-bottom: 20px;'>🏛️ 日干タイプ診断</h1>", unsafe_allow_html=True)
else:
    # 画像ファイルがフォルダにない場合でも美しく表示します
    st.markdown("<h1 style='color: #D4A373; font-size: 28px; letter-spacing: 2px; margin-bottom: 20px;'>🏛️ 日干タイプ診断</h1>", unsafe_allow_html=True)

st.markdown(
    "<p style='text-align: center; color: #5D4037; font-size: 14px; line-height: 1.6; margin-top: 15px;'>"
    "四柱推命（しちゅうすいめい）の根底にある「陰陽五行説」に基づき、<br>"
    "あなたが生まれ持った本質を表す<b>【自然界のシンボル（日干）】</b>を導き出します。"
    "</p>",
    unsafe_allow_html=True
)

# 生年月日選択
year = st.selectbox(
    "生まれ年",
    list(range(1900, date.today().year + 1))[::-1]
)
month = st.selectbox(
    "生まれ月",
    list(range(1, 13))
)
day = st.selectbox(
    "生まれ日",
    list(range(1, 32))
)

# 日干を正確に計算する関数（基準日を1900年1月1日＝甲戌に変更）
def nikkan(d):
    base = date(1900, 1, 1)  # 基準日（甲戌日）
    diff = (d - base).days
    
    # 10種類の天干に対応
    kashi_index = diff % 10
    kan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
    
    return kan[kashi_index]

# 日付の存在チェック（2月31日などのエラーを防止）
try:
    birth = date(year, month, day)
    is_valid_date = True
except ValueError:
    st.error("⚠️ 存在しない日付です。正しい生年月日を選択してください。")
    is_valid_date = False

# 計算の実行
if is_valid_date and st.button("自分の本質を導き出す ✨"):
    result = nikkan(birth)
    
    # 四柱推命の五行と陰陽のロジックに完全準拠したオリジナル肩書き
    princess_titles = {
        "甲": "🌲 【気高き大樹 of プリンセス】 （陽木）",
        "乙": "🌿 【しなやかな草花のフェアリー】 （陰木）",
        "丙": "☀️ 【世界を照らす太陽のクイーン】 （陽火）",
        "丁": "🔥 【静寂を灯すともしびのミスティック・ミューズ】 （陰火）",
        "戊": "⛰ 【悠然たるマウンテン・クイーン】 （陽土）",
        "己": "🌾 【慈愛とはぐくみの大地（マザー・プリンセス）】 （陰土）",
        "庚": "⚔️ 【不屈の意志を持つソード・ヴァルキリー（戦乙女）】 （陽金）",
        "辛": "💎 【光を秘めた至高のジュエル・プリンセス】 （陰金）",
        "壬": "🌊 【自由を愛するオーシャン・クイーン】 （陽水）",
        "癸": "💧 【世界を潤すミスティ・レイン（雨露のフェアリー）】 （陰水）"
    }
    
    # 各日干の「陰陽五行としての本来の姿」と「現代的解釈」を両立させた詳細解説
    meanings = {
        "甲": "<b>【自然界の姿：大樹】</b><br>大地にしっかりと根を張り、まっすぐ天に向かって伸びる大木のように、強い自立心と正義感を持つあなた。曲がったことが嫌いで、困難にも負けない凛とした強さを持っています。周囲をまとめ、人々を引っ張るリーダーとしての資質も抜群です。",
        "乙": "<b>【自然界の姿：草花】</b><br>野に咲く可憐な草花のように、親しみやすく調和を大切にするあなた。周囲を癒やす優しい魅力を持っています。一見控えめに見えて、実はどんな過酷な環境でもしなやかに生き抜く、抜群の粘り強さと適応能力（雑草魂）を秘めています。",
        "丙": "<b>【自然界の姿：太陽】</b><br>空高く輝き、地上をあまねく照らす太陽のようなあなた。そこにいるだけで周囲がパッと明るくなるような、圧倒的な存在感と華やかさがあります。情熱的で裏表がなく、常にみんなの中心に位置する天性の主役タイプです。",
        "丁": "<b>【自然界の姿：灯火・キャンドル】</b><br>暗闇の中に温かな光を灯すキャンドルや月明かりのようなあなた。非常に繊細で豊かな感性を持ち、深い思索を好む知性派です。内に秘めた情熱は誰よりも熱く、人々を優しく導くミステリアスな魅力を持っています。",
        "戊": "<b>【自然界の姿：山】</b><br>雄大にそびえ立つ山や岩石のようなあなた。とても心が広く、抜群の安定感と包容力を持っています。ちょっとしたことでは動じないマイペースさと頼もしさがあり、周囲の人々が自然と集まり頼いにする「安心の象徴」です。",
        "己": "<b>【自然界の姿：大地・田畑】</b><br>あらゆる作物を愛情たっぷりに育てる、豊かで優しい大地（畑）のようなあなた。誰に対してもおっとりと接し、困っている人を見捨てられない面倒見の良さがあります。多様な人の個性や才能を見出し、はぐくむ天才です。",
        "庚": "<b>【自然界の姿：鉄鋼・刀剣】</b><br>研ぎ澄まされた鋼（ハガネ）や鋭い刀剣のようなあなた。行動力と決断力にあふれ、一度決めた目標はブレずに最後までやり遂げるタフな心を持っています。自分を鍛える葛藤を乗り越え、自らの手で未来を切り拓く開拓者です。",
        "辛": "<b>【自然界の姿：宝石・砂金】</b><br>磨かれることで美しく光を放つ宝石のようなあなた。類まれなる美意識と、独自の洗練されたこだわりを持っています。繊細で傷つきやすい一面もありますが、試練を乗り越える（自分を磨く）たびに魅力が増し、本物のカリスマへと輝きます。",
        "壬": "<b>【自然界の姿：大海・大河】</b><br>スケールの大きい大海原や大河のようなあなた。自由をこよなく愛し、1つの場所にとどまらないダイナミックな冒険心を持っています。豊かな知性と、すべてを包み込んで変化させる包容力があり、世界を舞台に活躍できるスケール感があります。",
        "癸": "<b>【自然界の姿：雨露・湧水】</b><br>大地を優しく潤し、万物を育成する恵みの雨や朝露のようなあなた。とても純粋で、人の気持ちに寄り添える深い優しさを持っています。一見静かで控えめですが、非常に思慮深く、高い学習能力と知性を備えています。"
    }
    
    readings = {
        "甲": "きのえ", "乙": "きのと", "丙": "ひのえ", "丁": "ひのと", "戊": "つちのえ",
        "己": "つちのと", "庚": "かのえ", "辛": "かのと", "壬": "みずのえ", "癸": "みずのと"
    }
    
    # 各五行を意識した本格カラー
    colors = {
        "甲": "#27ae60",  # エメラルドグリーン（木・陽）
        "乙": "#2ecc71",  # リーフグリーン（木・陰）
        "丙": "#e74c3c",  # シャイニングレッド（火・陽）
        "丁": "#e67e22",  # キャンドルオレンジ（火・陰）
        "戊": "#d35400",  # テラコッタブラウン（土・陽）
        "己": "#f39c12",  # ウォームイエロー（土・陰）
        "庚": "#7f8c8d",  # クールシルバー（金・陽）
        "辛": "#9b59b6",  # アメジストパープル（金・陰）
        "壬": "#2980b9",  # コバルトブルー（水・陽）
        "癸": "#1abc9c"   # ミスティブルーグリーン（水・陰）
    }
    
    # 安全な埋め込み処理
    html_content = (
        "<div class=\"result-card\">"
        "<div style=\"font-size: 24px; font-weight: bold; color: #3E2723; margin-bottom: 10px;\">"
        "🔮 あなたの診断結果"
        "</div>"
        "<p style=\"font-size: 15px; color: #5D4037; line-height: 1.7; text-align: left; margin-bottom: 25px; background: #FAF7F2; padding: 15px; border-radius: 12px; border-left: 4px solid #D4A373;\">"
        "入力された生年月日から、東洋に伝わる伝統的な人間学・運命学である<b>【四柱推命】</b>の算出ロジックを用いて、あなたの本質を司る特別なエネルギー<b>【日干（にっかん）】</b>を割り出しました。<br><br>"
        "四柱推命の世界では、人はそれぞれ「生まれながらに大自然のいずれかの姿を宿している」と考えます。あなたの魂が持つ自然の姿は……"
        "</p>"
        f"<div style=\"background-color: #FCFBF9; border-radius: 20px; padding: 25px 15px; margin-bottom: 25px; border: 1px solid #EFEAE2; border-top: 5px solid {colors[result]};\">"
        f"<span style=\"font-size: 84px; line-height: 1; display: block; font-weight: bold; color: {colors[result]}; margin-bottom: 5px;\">"
        f"{result}"
        f"</span>"
        f"<span style=\"font-size: 18px; color: #5D4037; display: block; margin-bottom: 15px; font-weight: bold;\">"
        f"（{readings[result]}）"
        f"</span>"
        f"<span style=\"font-size: 20px; font-weight: bold; color: {colors[result]}; display: block;\">"
        f"{princess_titles[result]}"
        f"</span>"
        f"</div>"
        f"<div style=\"font-size: 15px; color: #3E2723; text-align: left; line-height: 1.8; background: #FFFDF9; border-radius: 15px; padding: 22px; border: 1px dashed #E8E2D5; margin-bottom: 20px;\">"
        f"{meanings[result]}"
        f"</div>"
        "<div style=\"font-size: 13px; color: #8D6E63; margin-top: 15px; line-height: 1.5;\">"
        "四柱推命が教える大自然からのメッセージ。<br>"
        "結果をスクリーンショットで保存して、ぜひ <b>#日干タイプ診断</b> でシェアしてね🤍"
        "</div>"
        "</div>"
    )
    
    st.markdown(html_content, unsafe_allow_html=True)
