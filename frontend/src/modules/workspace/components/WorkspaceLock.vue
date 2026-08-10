<template>

<button
class="lock"
@click="toggle"
>

<img
:src="locked ? closeIcon : openIcon"
/>

</button>


</template>



<script setup>


import {
computed
}
from "vue";


const props = defineProps({

locked:Boolean

});


const emit =
defineEmits([
"toggle"
]);



const openIcon =
"/images/unlock.png";


const closeIcon =
"/images/lock.png";



const toggle=()=>{

emit(
"toggle"
);

};


</script>



<style scoped>


.lock{


position:absolute;


left:30px;


bottom:30px;



width:50px;

height:50px;



border:none;


background:none;


cursor:pointer;



z-index:999;



}


.lock img{


width:100%;


height:100%;


}
</style>