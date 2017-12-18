// 1. Define route components.
// These can be imported from other files
var child_one = {
  template: "<p>이건 인스턴스 one 입니다.</p>"
}
var child_two = {
  template: "<p>이건 인스턴스 two 입니다.</p>"
}

// 2. Define some routes
// Each route should map to a component. The "component" can
// either be an actual component constructor created via
// Vue.extend(), or just a component options object.
// We'll talk about nested routes later.
var routes = [
  { path: "/one", component: child_one },
  { path: "/two", component: child_two },
]


// 3. Create the router instance and pass the `routes` option
// You can pass in additional options here, but let's
// keep it simple for now.
var router = new VueRouter({
  routes
})

// 4. Create and mount the root instance.
// Make sure to inject the router with the router option to make the
// whole app router-aware.
var app = new Vue({
  router
}).$mount("#app")

// Now the app has started!
