<script setup>
import {ref} from 'vue'
import {useRouter} from 'vue-router'
import axios from 'axios'
import Nav from "@/views/zujian/nav.vue";

let email = ref("")
let password = ref("")

let result1 = ref(false)
let result2 = ref(false)
let showPassword = ref(false); // 显隐

const router = useRouter()

// function => login
let login = () => {
  let reg_email = /^([a-zA-Z]|[0-9])(\w|\-)+@[a-zA-Z0-9]+\.([a-zA-Z]{2,4})$/
  result1 = !reg_email.test(email.value)
  if (!result1) {
    // console.log({email: email.value, name: name.value, password: password.value})
    axios.post('http://127.0.0.1:55555/login', {
      email: email.value,
      password: password.value
    }).then((res) => {
      // console.log(res.data)
      alert(res.data.msg)
      router.push({name: 'home', state: {userData: res.data}});
    })
  } else {
    console.log("error")
  }
}
// function => go to register
let register = () => {
  router.push('/register')
}
// // 是否显示密码设置
// let togglePasswordVisibility = () => {
//   showPassword.value = !showPassword.value;
// };
</script>

<template>
  <div class="mainpage">
	  <Nav/>
	  <div class="register-container">
            <div class="left-section">
				<!-- 二维码登录区域 -->
				<div class="qr-code">
					<label class="text1"><b>扫描二维码登录</b></label>
					<img src="/qrcode.jpg" alt="QR Code" />
					<label class="text2">关注官方<a href="#">公众号</a><br>获取最新讯息:D</label>
				</div>
            </div>
			<!-- 右侧内容部分 -->
		<div class="right-section">
			<!-- 原有的登录部分 -->
			<div class="passcord-message">
				登录 | Log in
			</div>
			<br>
			<div class="whole-border">

				<!-- 账号框部分 -->
				<div class="input-container">
					<label for="email">账号</label>
					<div>
						<input id="email" type="email" placeholder="请输入账号" v-model="email"/>
						<p class="email" v-show="result1">Not a valid email</p>
					</div>
				</div>

				<br>
				<!-- 密码框部分 -->
				<div class="input-container">
				  <label for="password">密码</label>
				  <div>
					<input id="password" :type="showPassword ? 'text' : 'password'" placeholder="请输入密码" v-model="password"/>
					<!-- 隐藏/显示密码按钮 待优化
					<button @click="togglePasswordVisibility">
					  {{ showPassword ? 'Hide' : 'Show' }} Password
					</button> -->
				  </div>
				  <p class="password" v-show="result2">Not a valid password</p>
				</div>
			</div>
			<div class="forget"><a href="#">忘记密码？</a></div>
			<div class="to">
				<button class="signup" @click="register">注册</button>
				<button class="login" @click="login">登录</button>
			</div>
		</div>
	  </div>
  </div>
</template>


<style scoped>
	.mainpage{
		background-image: url('../picture/bg2-4.jpg');
		background-size: cover;
		background-position: center;
		background-repeat: no-repeat;
		background-attachment: fixed;
		position: relative;
		z-index: 1;
		height: 100vh;
		width:100%;
    border: 1px solid darkgray;
	}
	.register-container {
	  display: flex;
	  max-width: 800px; /* 调整最大宽度 */
	  max-height: 1000px;
	  height: 300px;
	  margin: 10% auto;
	  margin-top: 170px;
	  padding: 37px;
	  border-radius: 8px;
	  text-align: left; /* 文字居左 */
	  background: rgba(255, 255, 255);
	  position: relative;
	}
	.register-container::before {
	  content: "";
	  position: absolute;
	  top: 0;
	  bottom: 0;
	  left: 40%; /* 将竖线放置在容器的中间 */
	  border-left: 1px solid darkgray;
	  height: 60%;
	  margin-top: 10%;
	  transform: translateX(-50%);
	}
	.left-section {
		width: 45%;
	}

	.qr-code{
		display: flex;
		flex-direction: column;
		align-items: center; /* 水平居中 */
		margin: auto; /* 左右居中 */
	}
	.text1{
		font-size:17px;
		 margin:10px;
		 margin-top:25px ;
		 margin-bottom:15px ;
		 text-align: center;
	}
	.text2{
		font-size:12px;
		 margin:10px;
		 line-height: 17px;
		 text-align: center;
	}
	.qr-code img {
	  width: 50%; /* 设置图片宽度为原来的一半 */
	  max-width: 100%; /* 图片最大宽度不超过容器宽度 */
	  max-height: 100%; /* 图片最大高度不超过容器高度 */
	  display: block; /* 去除底部空白 */
	  border: 1px solid darkgray;
	  border-radius: 8px;
	  padding:1px;
	}

	.passcord-message{
		font-weight:bolder;
		font-size:30px;
		text-align: center;
		margin-top: 25px;
		margin-bottom: 10px;
	}
	.whole-border{
		border: 1px solid darkgray;
		border-radius: 11px;
		display: flex;
		  flex-direction: column;
		  align-items: center;
		  justify-content: center;
		  height: 35%;
		  width: 360px;
		  position:relative;
	}
	.whole-border::before {
	  content: "";
	  position: absolute;
	  top: 50%;
	  left: 0;
	  right: 0;

	  border-top: 1px solid #ccc;
	  z-index: 1;
	}
	.input-container {
	  display: flex;
	  width: 200px;
	  align-items: center;
	  position: relative;
	  margin-right: 80px;
	  margin-left: -10px;
	}
	.input-container button {
	  position: relative;
	  float: right; /* 或者使用 margin-left: auto; */
	  align-self: center; /* 垂直居中对齐 */
	  transform: translateY(-110%);
	  background: none;
	  border: none;
	  cursor: pointer;
	  color: deeppink;
	}
	.input-container div {
		display: flex;
		align-items: center;
	}
	label {
		line-height: 20px;/* add */
		display: inline-block;
		margin-right: 20px;
		white-space: nowrap; /* 防止文字换行 */
		font-size: 15px;
	}
	input {
		width: 230px;
		flex: 1;
		font-size: 15px;
		padding: 8px;
		box-sizing: border-box;
		border: none;
		/* background-color: #f2f2f2; */
	}
	button {
	  margin-top:10px;
	  padding: 10px;
	  background-color: royalblue;
	  color: white;
	  border: none;
	  border-radius: 11px;
	  cursor: pointer;
	  width: 170px;
	}
	.to {
	  display: flex;
	  justify-content: space-between;
	}
	button:hover {
	  background-color: darkblue;
	}
	p {
	  color: red;
	  margin-top: 5px;
	  display: none;
	}
	a{
		color:dodgerblue;
	}
	.forget{
		margin-left: 285px;
		margin-top: 10px;
	}
	.forget a{
		color:darkgrey;
		text-decoration: underline;
	}
</style>
