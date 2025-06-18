<script setup>
import {ref} from 'vue'
import {useRouter} from "vue-router";
import axios from 'axios'
import Nav from "@/views/zujian/nav.vue";

let name = ref("")
let email = ref("")
let password = ref("")

let result0 = ref(false)
let result1 = ref(false)
let result2 = ref(false)
let router = useRouter()

// function => go to login
let login = () => {
  router.push('/login')
}

// function => register
let register = () => {
  let reg_email = /^([a-zA-Z]|[0-9])(\w|\-)+@[a-zA-Z0-9]+\.([a-zA-Z]{2,4})$/
  result1 = !reg_email.test(email.value)
  if (!result1) {
    console.log({email: email.value, name: name.value, password: password.value})
    axios.post('http://127.0.0.1:55555/register', {
        email: email.value,
        name: name.value,
        password: password.value
    }).then((res) => {
      // console.log(res.data)
      alert(res.data.msg)
      router.push('/login')
    }).catch((error) => {
      console.log(error)
    })
  } else {
    console.log("error")
  }
}
</script>

<template>

	<div class="mainpage">
	  <div class="register-container">
			<div class="left-section">

			</div>
      <Nav/>

			<div class="right-section">
				<div class="toptext">注册 | Sign in</div>
				<br>
				<div class="input-container">
					<label for="name"> 昵称</label>
					<input id="name" type="text" placeholder="请输入昵称" v-model="name"/>
					<p class="name" v-show="result0">Not a valid name</p>
				</div>

				<div class="input-container">
					<label for="email">邮箱/手机号/学号</label>
					<input id="email" type="email" placeholder="请输入邮箱/手机号/学号" v-model="email"/>
					<p class="email" v-show="result1">Not a valid email</p>
				</div>

				<div class="input-container">
					<label for="password">密码</label>
					<input id="password" type="password" placeholder="请设置密码" v-model="password"/>
					<p class="password" v-show="result2">Not a valid password</p>
				</div>

				<div class="to">
					<button @click="register">提交</button>
					<button @click="login" class="login">已有账号？去登录</button>
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
    margin: 0;
    border: 1px solid #ccc;
	}
	.register-container {
		display: flex;
		max-width: 800px; /* 调整最大宽度 */
		max-height: 1000px;
		height: 400px;
		margin: 10% auto;
		padding: 20px;
		border-radius: 8px;
		/* background: rgba(255, 255, 255);*/
		background-image: url('../picture/rgst.png');
		background-size: cover;
		background-repeat: no-repeat;
		background-position: center;

	}
	.left-section {
		width: 55%;
	}
	.right-section{
		width: 60%;
	}
	.toptext{
		font-weight: bolder;
		font-size: 37px;
		margin-top: 25px;
		margin-bottom: -5px;
	}
	.input-container {
		margin-bottom: 15px;
		margin-top: 10px;
	}
	.input-container label {
		display: block;
		margin-bottom: 1px;
		font-weight: bold;
	}

	input {
		width: 80%;
		padding: 10px;
		box-sizing: border-box;
		margin-bottom: 5px;
		display: flex;
		align-items: center;
	 }

	button {
	  margin-top:10px;
	  margin-right: 20px;
	  padding: 10px;
	  background-color: royalblue;
	  color: white;
	  border: none;
	  border-radius: 11px;
	  cursor: pointer;
	  width: 160px;
	}
	.login{
	  background-color: darkgrey;
	}

	button:hover {
		background-color: darkblue;
	}

	p {
	color: red;
	margin-top: 5px;
	display: none;
	}
</style>
