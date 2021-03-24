<template>
    <div>
        <h1>
            <button @click="GetApiInput">Show</button>
            <canvas id="myChart" width="1000" height="1000"></canvas>
            <p>{{item}}</p>
        </h1> 
    </div>
</template>
<script> 
import item from './App'
import Chart from 'chart.js'
import Vue from 'vue';
    export default { 
        props:[
            'item'     
        ],
        data: () => ({
        diagramInput: [],
        diagramLabels : [],
        lab: []
    
        }),
        methods:{
            GetApiInput(){
            Vue.axios.get('http://127.0.0.1:1339/api/v1/csv/channel?item=Channel%202')
            .then((response)=>{
                this.diagramInput = response.data.channel.data;
                this.diagramLabels = response.data.channel.count;
                console.log(this.diagramInput);
                console.log(this.diagramLabels)
                this.Diagram()
            })
                
        },
            Diagram(){
                var myChartObject = document.getElementById('myChart');
                
                new Chart(myChartObject,{
                    type: 'line',
                    data: {
                        labels: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],
                        datasets: [{
                            label: "Datensatz Nummer 1",
                            data: this.diagramInput
                        }]
                    }
                });
                 
            }
    }

    }

</script>