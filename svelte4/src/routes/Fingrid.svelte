<script>
    import DataTable from "./DataTable.svelte";
    import BarChart from "./BarChart.svelte";
    import LineChart from "./LineChart.svelte";
    import { onMount } from "svelte";

    let windData;
    let prodData;
    let consData;
    let tempData;
    let date;

    onMount(() => (date = new Date().toISOString().slice(0, 10)));

    $: date != null ? windGeneration(date) : null;
    function windGeneration(date) {
        fetch(
            `http://localhost:5000/windgeneration?startTime=${date}T00:00:00Z&endTime=${date}T23:00:00Z`,
        )
            .then((response) => {
                return response.json();
            })
            .then((result) => {
                windData = result.data;
                windData = windData.map((value) => {
                    let startTime = new Date(value.startTime);
                    startTime.setUTCHours(startTime.getUTCHours() - 3);
                    value.startTime = startTime;
                    let endTime = new Date(value.endTime);
                    endTime.setUTCHours(endTime.getUTCHours() - 3);
                    value.endTime = endTime;
                    return value;
                });
                windData = windData.filter((value, index) => index % 4 == 0);
            });
    }

    $: date != null ? production(date) : null;
    function production(date) {
        fetch(
            `http://localhost:5000/production?startTime=${date}T00:00:00Z&endTime=${date}T23:45:00Z`,
        )
            .then((response) => {
                return response.json();
            })
            .then((result) => {
                prodData = result.data;
                prodData = prodData.map((value) => {
                    let startTime = new Date(value.startTime);
                    startTime.setUTCHours(startTime.getUTCHours() - 3);
                    value.startTime = startTime;
                    let endTime = new Date(value.endTime);
                    endTime.setUTCHours(endTime.getUTCHours() - 3);
                    value.endTime = endTime;

                    return value;
                });
                prodData = prodData.filter((value, index) => {
                    return index % 4 == 0;
                });
            });
    }

    $: date != null ? consumption(date) : null;
    function consumption(date) {
        fetch(
            `http://localhost:5000/consumption?startTime=${date}T00:00:00Z&endTime=${date}T23:45:00Z`,
        )
            .then((response) => {
                return response.json();
            })
            .then((result) => {
                consData = result.data;
                consData = consData.map((value) => {
                    let startTime = new Date(value.startTime);
                    startTime.setUTCHours(startTime.getUTCHours() - 3);
                    value.startTime = startTime;
                    let endTime = new Date(value.endTime);
                    endTime.setUTCHours(endTime.getUTCHours() - 3);
                    value.endTime = endTime;

                    return value;
                });
                consData = consData.filter((value, index) => {
                    return index % 4 == 0;
                });
            });
    }

    $: date != null ? temperature(date) : null;
    function temperature(date) {
        let firstTempData = [];
        let secondTempData = [];
        tempData = [];

        // API antaa maksimissaan 254 arvoa per haku joten jaetaan haku kahteen osaan
        // Fetch data for 00:00-12:00
        fetch(
            `http://localhost:5000/temperature?startTime=${date}T00:00:00Z&endTime=${date}T12:00:00Z`,
        )
            .then((response) => response.json())
            .then((result) => {
                firstTempData = result.data;
                console.log("firstTempData", firstTempData);

                // Fetch data for 12:00-24:00
            });
        fetch(
            `http://localhost:5000/temperature2?startTime=${date}T12:00:00Z&endTime=${date}T23:59:59Z`,
        )
            .then((response) => response.json())
            .then((result) => {
                secondTempData = result.data;
                console.log("secondTempData", secondTempData);

                tempData = firstTempData.concat(secondTempData);

                tempData = tempData.map((value) => {
                    let startTime = new Date(value.startTime);
                    let endTime = new Date(value.endTime);

                    startTime.setUTCHours(startTime.getUTCHours() - 3);
                    endTime.setUTCHours(endTime.getUTCHours() - 3);

                    value.startTime = startTime;
                    value.endTime = endTime;

                    return value;
                });
                tempData = tempData.filter((value, index) => {
                    return index % 20 == 0;
                });
                console.log("tempData after", tempData);
            });
    }
</script>

<div class="header">
    <h1>Electricity production in Finland</h1>
</div>
<div class="main">
    <p>Choose the date <input type="date" bind:value={date} /></p>
    <DataTable {windData} />
    <BarChart {prodData} {consData} />
    <LineChart {tempData} />
</div>

<style>
    .header {
        background-color: goldenrod;
        padding: 10px;
        text-align: center;
        font-family: tahoma;
    }
    .main {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
</style>
