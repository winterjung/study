var Login = {
  template: `
    <div>
      로그인 화면
      <router-view></router-view>
    </div>
  `,
};
var LoginForm = {
  template: `
    <form action="/" method="post">
      <div>
          <label for="account">E-mail : </label>
          <input type="email" id="account">
      </div>
      <div>
          <label for="password">Password : </label>
          <input type="password" id="password">
      </div>
    </form>
  `,
};
var List = {
  template: `
    <div>
      리스트
      <router-view></router-view>
    </div>
  `,
};
var ListItems = {
  template: `
    <ul>
      <li>python</li>
      <li>cython</li>
      <li>cpython</li>
      <li>모두 다르답니다</li>
    </ul>
  `,
};

var routes = [{
    path: '/login',
    component: Login,
    children: [{
      path: '',
      component: LoginForm
    }]
  },
  {
    path: '/list',
    component: List,
    children: [{
      path: '',
      component: ListItems
    }]
  }
];

var router = new VueRouter({
  routes
});

var app = new Vue({
  router
}).$mount('#app');
