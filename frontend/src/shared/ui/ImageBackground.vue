<template>

<div
 class="image-background"
 :style="style"
>

<slot />

</div>

</template>


<script setup>

import {computed} from "vue";


const props = defineProps({

 src:{
  type:String,
  default:""
 },

 size:{
  type:String,
  default:"cover"
 },

 position:{
  type:String,
  default:"center"
 }

});


const style = computed(()=>({

 backgroundImage:`url(${props.src})`,

 backgroundSize:props.size,

 backgroundPosition:props.position

}));


</script>


<style scoped>

.image-background{

 width:100%;

 height:100%;

 background-repeat:no-repeat;

}

</style>