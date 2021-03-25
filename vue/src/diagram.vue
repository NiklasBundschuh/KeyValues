<template>
    <div>
        <h1>
            <button @click="GetApiInput">Show</button>
            <canvas id="myChart" width="700" height="700"></canvas>
            
        </h1> 

    </div>
</template>
<script> 
import Chart from 'chart.js'
import Vue from 'vue';

    export default { 
        
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
                console.log(this.diagramInput);
                this.Diagram()
            })
                
        },
            Diagram(){
                var myChartObject = document.getElementById('myChart');
                var counter = 1
                while(counter <= 390){
                    this.diagramLabels.push(counter)
                    counter++
                }
                console.log(this.diagramLabels)
                new Chart(myChartObject,{
                    type: 'line',
                    data: {
                        labels: this.diagramLabels,
                        datasets: [{
                            label: "Datensatz Nummer 1",
                            backgroundColor: 'rgba(65,105,225,0.4)',
                            borderColor: 'rgba(100,105,225,1)',
                            data: this.diagramInput
                        }],
                        options:{
                                scales:{
                                    x:{
                                        type: 'timeseries',
                                    },
                                    xAxes: [{
                                        ticks: {
                                            suggestedMax: 390
                                        }
                                    }]
                                }
                            }
                    }
                });
                 
            }
    }

    }

</script>