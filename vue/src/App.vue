
<template>
  <div id="app">
    <div class="lds-roller" v-if="loading"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
    <h1>KeyValues</h1>
    <button @click="loadHeader">HeaderDict</button>
    <ul>   
      <select id ="Header" size="5" @change="changeItem">
      </select>
    </ul>
    <div class="action">
      <diagram :diagramInput="Channeldata" :channelLabel="item"></diagram>
  </div>
  </div>
</template>
<script>
import Vue from 'vue';



  //<app-diagram :diagramInput='Channeldata'></app-diagram>
  export default {
    name: 'App',
    data: () => ({
      loading: false,
      Header: [],
      data: [],
      item: "",
      Channeldata: []
      
      
      
      
    }),

    methods: {
      async loadHeader(){
        this.loading = true;
        let apiUrl = 'http://127.0.0.1:1339/api/v1/csv/data';
        console.log("Header Button wurde geklickt");
        try{
          //await will stop async until the promise is fulfilled
          let response = await this.axios.get(apiUrl);
          console.log(response);
          this.Header = response.data.channels;
          
          
          //get reference of section in HTML
          var channelSection = document.getElementById("Header");

          //populate section
          this.Header.forEach(function(item, index){
            var opt = document.createElement("option");
            opt.value = index;
            opt.innerHTML = item;
            channelSection.appendChild(opt);
          });
        }catch (e){
          console.error(e);
        } 
        this.loading = false;
      },
 
      changeItem(){
        //get reference of section in HTML
        var channelSection = document.getElementById("Header");
        var index = channelSection.selectedIndex;
        this.item = channelSection.options[index].text;
        console.log(this.item);

        var dataForm = new FormData
        dataForm.append("item", this.item)
        var channelUrl = "http://127.0.0.1:1339/api/v1/csv/channel?item="+this.item;
        Vue.axios.get(channelUrl)
        .then((response)=>{
          this.Channeldata = response.data.channel.data
        
          
        })
        
        


        //var diagram = document.getElementById("app-diagram");
        //diagram
        
      }
    }
  }

</script>

<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
  .action{
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
  }
 /*The CSS code for the loading animation */
  .lds-roller {
    display: inline-block;
    position: relative;
    width: 80px;
    height: 80px;
  }
  .lds-roller div {
    animation: lds-roller 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
    transform-origin: 40px 40px;
  }
  .lds-roller div:after {
    content: " ";
    display: block;
    position: absolute;
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #000;
    margin: -4px 0 0 -4px;
  }
  .lds-roller div:nth-child(1) {
    animation-delay: -0.036s;
  }
  .lds-roller div:nth-child(1):after {
    top: 63px;
    left: 63px;
  }
  .lds-roller div:nth-child(2) {
    animation-delay: -0.072s;
  }
  .lds-roller div:nth-child(2):after {
    top: 68px;
    left: 56px;
  }
  .lds-roller div:nth-child(3) {
    animation-delay: -0.108s;
  }
  .lds-roller div:nth-child(3):after {
    top: 71px;
    left: 48px;
  }
  .lds-roller div:nth-child(4) {
    animation-delay: -0.144s;
  }
  .lds-roller div:nth-child(4):after {
    top: 72px;
    left: 40px;
  }
  .lds-roller div:nth-child(5) {
    animation-delay: -0.18s;
  }
  .lds-roller div:nth-child(5):after {
    top: 71px;
    left: 32px;
  }
  .lds-roller div:nth-child(6) {
    animation-delay: -0.216s;
  }
  .lds-roller div:nth-child(6):after {
    top: 68px;
    left: 24px;
  }
  .lds-roller div:nth-child(7) {
    animation-delay: -0.252s;
  }
  .lds-roller div:nth-child(7):after {
    top: 63px;
    left: 17px;
  }
  .lds-roller div:nth-child(8) {
    animation-delay: -0.288s;
  }
  .lds-roller div:nth-child(8):after {
    top: 56px;
    left: 12px;
  }
  @keyframes lds-roller {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }


</style>


