<template>
  <div class="Navbar">
    <nav class="navbar">
      <div class="left">
        <div>
          <a class="logo" href="https://www.cdut.edu.cn/"><img src="/favicon.ico" style="height: 57px"></a>
        </div>
        <div class="anniu">
          <a href="/">首页</a>
          <a href="/store">商城</a>
          <a href="/cart">购物车</a>
        </div>
      </div>
      <div class="right">
        <div v-if="isAuthenticated" class="user-info">
          <!-- 显示用户头像等信息 -->
          <img :src="user.avatar" alt="User Avatar" class="avatar"/>
          <span class="username">{{ user.name }}</span>
          <div class="logout-btn" @click="logout">登出</div>
        </div>
        <div v-else class="login-btn" @click="goToLogin">登入</div>
      </div>
    </nav>
  </div>
  <router-view></router-view>
</template>
<!--------------------------------------------------------------------------------------------------------------------->
<script setup>
import {ref, onMounted} from "vue";
import {useRouter} from "vue-router";

let router = useRouter()

let isAuthenticated = ref(false)
let user = ref({name: "", avatar: ""})

const route = useRouter();
//function => go to the login page
let goToLogin = () => {
  // TODO:there is a problem about the route.push('/login')
  router.push('/login')
  // location.href = '/login'
}

//function => logout
let logout = () => {
  // show the username and avatar
  isAuthenticated.value = false;

  // if user not exist, delete all the user object
  delete history.state.userData.user;

  // refresh history.state
  history.replaceState(history.state, '');
  router.push('/')
}

// after the component mounted ,and loading the data
onMounted(() => {
  try{
  if (history.state.userData.user) {
    user.value.name = history.state.userData.user.user.name
    user.value.avatar = history.state.userData.user.user.avatar
    isAuthenticated.value = true
    console.log('User Data:', history.state.userData);
  }}catch (e){
    console.log(e)
  }
});
</script>
<!--------------------------------------------------------------------------------------------------------------------->
<style scoped>
.anniu {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: nowrap;
  margin-left: 50px;
}

.anniu a {
  width: 130px;
}
.left {
  justify-content: left;
  display: flex;
  flex-wrap: nowrap;
}

.right {
  justify-content: right;
}

.left a:hover {
  color: #45a049;
}

.navbar {
  background-color: rgba(255, 255, 255, 0.8);
  padding: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #ccc;
  border-radius: 15px;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
}

.navbar a {
  margin-left: 20px;
  margin-right: 10px;
  padding: inherit;
  font-size: 2.5em;
  font-family: fantasy;
  text-decoration: none;
  color: #333;
}

.login-btn, .logout-btn {
  position: relative;
  right: 0;
  padding: 8px;
  background-color: royalblue;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  width:88px ;
  text-align: center;
}


.login-btn:hover {
  background-color: darkblue;
}

.logout-btn:hover {
  background-color: darkblue;
}

.avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  margin-right: 8px;
}

.username {
  margin-right: 8px;
}

.user-info {
  display: flex;
  align-items: center;
}
</style>
