import streamlit as st
import joblib
import pandas as pd

# 学習済みモデルと入力項目を読み込む
model = joblib.load("sake_model.joblib")
features = joblib.load("sake_features.joblib")

st.title("日本酒の甘辛傾向予測アプリ")

st.write(
    "日本酒の成分情報から、甘辛度の目安を予測します。"
)

st.info(
    "このアプリは日本酒度を使わずに予測します。"
    "予測値は参考値であり、実際に飲んだときの味わいを"
    "保証するものではありません。"
)

# 入力フォーム
with st.form("sake_input_form"):
    rice_polishing_rate = st.number_input(
        "精米歩合（%）",
        min_value=1.0,
        max_value=100.0,
        value=60.0,
        step=1.0
    )

    alcohol_rate = st.number_input(
        "アルコール度数（%）",
        min_value=0.0,
        max_value=30.0,
        value=16.0,
        step=0.5
    )

    amino_acid_content = st.number_input(
        "アミノ酸度",
        min_value=0.0,
        max_value=10.0,
        value=1.2,
        step=0.1
    )

    titratable_acidity = st.number_input(
        "酸度",
        min_value=0.0,
        max_value=10.0,
        value=1.3,
        step=0.1
    )

    submitted = st.form_submit_button("甘辛度を予測する")

if submitted:
    input_data = pd.DataFrame([{
        "rice_polishing_rate": rice_polishing_rate,
        "alcohol_rate.mean": alcohol_rate,
        "amino_acid_content.mean": amino_acid_content,
        "titratable_acidity.mean": titratable_acidity
    }])

    # 学習時と同じ項目・順番で予測する
    input_data = input_data[features]
    prediction = model.predict(input_data)[0]

    st.subheader("予測結果")
    st.metric("予測甘辛度", f"{prediction:.2f}")

    if prediction < -0.5:
        st.write("予測上は、比較的辛口寄りです。")
    elif prediction > 0.5:
        st.write("予測上は、比較的甘口寄りです。")
    else:
        st.write("予測上は、甘辛度の中間付近です。")

    st.caption(
        "甘口・辛口の区分は、このアプリ独自の目安です。"
        "実際の味わいを直接判定するものではありません。"
    )