

'use strict';
const e = React.createElement;

function App() {

  return (
    <div style={"width: 380px"}>
    <crypto-converter-widget
       live
       shadow
       symbol
       fiat="united-states-dollar"
       crypto="bitcoin"
       amount="1"
       border-radius="0.60rem"
       background-color="#383a59"
       decimal-places="2"><a 
       href="https://cr.today/" 
       rel="noopener">Converter Widget</a></crypto-converter-widget>
    <a href="https://co-w.io/">co-w.io</a>
    <script src="https://cdn.jsdelivr.net/gh/dejurin/crypto-converter-widget/dist/latest.min.js" async></script>
  </div>
  );
}

const domContainer = document.querySelector('#reactAppContainer');
ReactDOM.render(
  e(App),
  domContainer
);