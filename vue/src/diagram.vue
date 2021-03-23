<template>
    <div>
        <h1>
            <ul>
                <li v-for="diagramInput in diagramInputs" :key="diagramInput">{{ diagramInput }}</li>
            </ul>    
        </h1> 
    </div>
</template>
<script> 
import Vue from 'vue';
    export default {    
        name: 'Diagram',
        data: () => ({
            diagramInputs: []
        }),

        mounted(){
            Vue.axios.get('http://127.0.0.1:1339/api/v1/csv/channel?item=Channel%202')
            .then((response)=>{
                this.diagramInput = response.data.channel.data;
                console.log(response.data.channel.data);
            })
                
        }

    }

</script>