# @CODING   : UTF-8
# @VERSION  : 1.0
# @AUTHOR   : Huangxuan
# @FILE     : main.py
# @TIME     : 2025/5/7-16:33

import streamlit as st
from utils import generate_script

st.title("视频脚本一键生成器")

with st.sidebar:
    deepseek_api_key = st.text_input("请输入DEEPSEEK API密钥：", type="password")
    st.markdown("[获取DEEPSEEK API密钥](https://platform.deepseek.com/api_keys)")

subject = st.text_input("请输入视频主题：")
video_length = st.number_input("请输入视频的大致时长(单位:分钟)：", min_value=0.1, step=0.1)
creativity = st.slider("请选择视频的创意程度：", value=0.2, min_value=0.0, max_value=1.2, step=0.1)
submitted = st.button("生成脚本")

if submitted and not deepseek_api_key:
    st.info("请输入你的DEEPSEEK API密钥！")
    st.stop()
if submitted and not subject:
    st.info("请输入视频的主题！")
    st.stop()
if submitted and video_length < 0.1:
    st.info("视频时长需要大于或等于0.1")
    st.stop()
if submitted:
    with st.spinner("AI正在思考，生成视频脚本，请稍等..."):
        search_result, title, script = generate_script(subject, video_length, creativity, deepseek_api_key)
    st.success("视频脚本已生成！")
    st.subheader("视频主题：")
    st.write(title)
    st.subheader("视频脚本：")
    st.write(script)
    with st.expander("维基百科搜索结果"):
        st.info(search_result)


