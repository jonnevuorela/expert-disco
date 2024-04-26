<script>
    import chartjs from "chart.js/auto";
    import { beforeUpdate, onMount } from "svelte";
    export let tempData;
    let chartCanvas;
    let chart;

    function drawCanvas() {
        if (tempData) {
            let labels = tempData.map((value) => {
                let startTime = new Date(value.startTime);
                return `${startTime.getHours().toString().padStart(2, "0")}:00`;
            });
            let myData = tempData.map((value) => value.value);
            if (chart) chart.destroy();
            let ctx = chartCanvas.getContext("2d");
            chart = new chartjs(ctx, {
                type: "line",
                data: {
                    labels: labels,
                    datasets: [
                        {
                            label: "Lämpötila Oulussa",
                            data: myData,
                            backgroundColor: "rgba(0, 255, 255, 1)",
                            borderColor: "rgba(0, 0, 0, 1)",
                            borderWidth: 1,
                        },
                    ],
                },
            });
        }
    }
    onMount(drawCanvas);
    beforeUpdate(drawCanvas);
</script>

<h3>Temperature in Oulu</h3>
<div>
    <canvas bind:this={chartCanvas} />
</div>

<style>
    div {
        border: 1px solid black;
        border-collapse: collapse;
        background-color: sandybrown;
        box-shadow: 5px 5px 10px black;
        width: 70rem;
        height: 50vh;
        margin-bottom: 5rem;
    }
</style>
