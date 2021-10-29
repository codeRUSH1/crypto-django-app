

'use strict';
const e = React.createElement;

function App() {

   function registerBtn() {
        window.location.href = "/register";
       }

   function loginBtn() {
    window.location.href = "/login";
   }

   function convertBtn() {
    window.location.href = "/convert";
   }

  return (
      <div>
<button class="button-64"  onClick={convertBtn} role="button"><span class="text">Convert Crypto</span></button>
<button class="button-64" onClick={registerBtn} role="button"><span class="text">Register</span></button>
<button class="button-64" onClick={loginBtn} role="button"><span class="text">Login</span></button>
      </div>
  );
}

const domContainer = document.querySelector('#reactAppContainer');
ReactDOM.render(
  e(App),
  domContainer
);
