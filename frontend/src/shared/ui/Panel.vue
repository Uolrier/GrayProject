<template>
  <div
    class="gray-panel"
    :style="panelStyle"
  >
    <slot />
  </div>
</template>


<script setup>

import { computed } from "vue";


const props = defineProps({

  background:{
    type:String,
    default:""
  },

  opacity:{
    type:Number,
    default:0.85
  },

  radius:{
    type:Number,
    default:16
  }

});


const panelStyle = computed(()=>({

  backgroundColor:`rgba(255,255,255,${props.opacity})`,

  backgroundImage: props.background
    ? `url(${props.background})`
    : "none",

  borderRadius:`${props.radius}px`

}));


</script>


<style scoped>

.gray-panel{

  width:100%;

  height:100%;

  overflow:hidden;

  backdrop-filter:blur(10px);

}

</style>