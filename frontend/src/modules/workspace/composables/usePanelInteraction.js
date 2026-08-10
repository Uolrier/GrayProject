import { ref } from "vue";


export function usePanelInteraction(panel, emit, locked){


    const dragging = ref(false);

    const resizing = ref(false);

    const rotating = ref(false);



    const offset = ref({
        x:0,
        y:0
    });



    const resizeStart = ref({

        x:0,

        y:0,

        width:0,

        height:0

    });
    const rotateStart = ref({
        angle:0,
        startAngle:0
    });
    function startDrag(e){
        dragging.value=true;
        offset.value.x =
            e.clientX -
            panel.position.x;
        offset.value.y =
            e.clientY -
            panel.position.y;
        window.addEventListener(
            "mousemove",
            onDrag
        );
        window.addEventListener(
            "mouseup",
            stopDrag
        );
    }
    function onDrag(e){
        if(!dragging.value)
            return;
        emit(
            "move",
            {
                x:
                e.clientX -
                offset.value.x,
                y:
                e.clientY -
                offset.value.y
            }
        )
    }
    function stopDrag(){
        dragging.value=false;
        window.removeEventListener(
            "mousemove",
            onDrag
        );
        window.removeEventListener(
            "mouseup",
            stopDrag
        );
    }
    function startResize(e){
        resizing.value=true;
        resizeStart.value={
            x:e.clientX,
            y:e.clientY,
            width:panel.width,
            height:panel.height,
            ratio:
            panel.width / panel.height
        };
        window.addEventListener(
            "mousemove",
            onResize
        );
        window.addEventListener(
            "mouseup",
            stopResize
        );
    }
    function onResize(e){
        if(!resizing.value)
            return;
        let width =
            resizeStart.value.width
            +
            e.clientX -
            resizeStart.value.x;
        let height =
            resizeStart.value.height
            +
            e.clientY -
            resizeStart.value.y;
        // Shift 保持比例
        if(e.shiftKey){
            height =
                width /
                resizeStart.value.ratio;
        }
        emit(
            "resize",
            {
                width,
                height
            }
        );
    }
    function stopResize(){
        resizing.value=false;
        window.removeEventListener(
            "mousemove",
            onResize
        );
        window.removeEventListener(
            "mouseup",
            stopResize
        );
    }
    function startRotate(e){
        rotating.value=true;
        const rect =
            e.currentTarget
            .parentElement
            .getBoundingClientRect();
        const centerX =
            rect.left +
            rect.width/2;
        const centerY =
            rect.top +
            rect.height/2;
        rotateStart.value={
            angle:
            panel.rotate,
            startAngle:
            Math.atan2(
                e.clientY-centerY,
                e.clientX-centerX
            )
        };
        window.addEventListener(
            "mousemove",
            onRotate
        );
        window.addEventListener(
            "mouseup",
            stopRotate
        );
    }
    function onRotate(e){
        if(!rotating.value)
            return;
        const rect =
            document
            .querySelector(
                `[data-panel-id="${panel.id}"]`
            )
            .getBoundingClientRect();
        const centerX =
            rect.left+
            rect.width/2;
        const centerY =
            rect.top+
            rect.height/2;
        const currentAngle =
            Math.atan2(
                e.clientY-centerY,
                e.clientX-centerX
            );
        const delta =
            currentAngle -
            rotateStart.value.startAngle;
        let degree =
            rotateStart.value.angle
            +
            delta*180/Math.PI;
        // Shift 吸附90度
        if(e.shiftKey){
            degree =
                Math.round(
                    degree / 90
                )
                *
                90;
        }
        emit(
            "rotate",
            degree
        );
    }
    function stopRotate(){
        rotating.value=false;
        window.removeEventListener(
            "mousemove",
            onRotate
        );
        window.removeEventListener(
            "mouseup",
            stopRotate
        );
    }
    return {
        startDrag,
        startResize,
        startRotate
    };
}