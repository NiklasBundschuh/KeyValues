<template>
    <div>
        <h1>
            <button @click="Diagram">Show</button>
            <canvas id="myChart" width="700" height="700"></canvas>
        </h1> 
    </div>
</template>
<script> 
import Chart from 'chart.js'


    export default { 
        props:{
            diagramInput:{
                type: Array,
                required: true
            },
            channelLabel:{
                type: String,
                required: true
            }

        },
        name: 'diagram',
        data: () => ({
        diagramLabels : [],
        lab: [],
      
        }),

        methods:{
            Diagram(){
                console.log(this.diagramInput)
                var myChartObject = document.getElementById('myChart');
                var counter = 1
                if (this.diagramLabels.length === 0){
                    while(counter <= 390){
                        this.diagramLabels.push(counter);
                        counter++;
                    }
                }
                console.log(this.diagramLabels);
                new Chart(myChartObject,{
                    type: 'line',
                    data: {
                        labels: this.diagramLabels,
                        datasets: [{
                            label: this.channelLabel,
                            backgroundColor: 'rgba(65,105,225,0.4)',
                            borderColor: 'rgba(100,105,225,1)',
                            data: this.diagramInput,
                            
                        }],
                        options:{
                                scales:{
                                    x:{
                                        type: 'timeseries',
                                    },
                                    xAxes: [{
                                        ticks: {
                                            suggestedMax: 10000
                                        }
                                    }]
                                }
                            }
                      
                    }
      
                })
            
                 
            }
    }
    }
    

</script>