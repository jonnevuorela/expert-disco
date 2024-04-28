<script>
    import { onMount } from "svelte";

    const url = "https://rata.digitraffic.fi/api/v2/graphql/graphql";
    let schedule;
    let junat;
    let foo;
    let bar;
    let asemat = { nimi: "", lyhenne: "" };
    let userInput = { id: "", station: " ", date: "" };
    //$: console.log(trains)
    let inputId;
    $: console.log("inputId", inputId);

    function getOptions() {
        function getAsemat() {
            fetch(`https://rata.digitraffic.fi/api/v1/metadata/stations`, {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    "Accept-Encoding": "gzip",
                },
            })
                .then((response) => {
                    if (!response.ok) {
                        throw new Error(
                            `HTTP error! status: ${response.status}`,
                        );
                    }
                    return response.json();
                })
                .then((result) => {
                    asemat = result.reduce((acc, item) => {
                        acc[item.stationName] = item.stationName;
                        return acc;
                    }, {});
                });
        }
        function getJunat() {
            fetch(`https://rata.digitraffic.fi/api/v1/live-trains/`, {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                    "Accept-Encoding": "gzip",
                },
            })
                .then((response) => {
                    if (!response.ok) {
                        throw new Error(
                            `HTTP error! status: ${response.status}`,
                        );
                    }
                    return response.json();
                })
                .then((result) => {
                    junat = result.map((item) => item.trainNumber);
                });
        }
        getAsemat();
        getJunat();
    }
    function fetchData() {
        const q1 = {
            query: `{
              train(
                trainNumber: ${userInput.id}
                departureDate: "${userInput.date}"
                where: {timeTableRows: {contains: {station: {name: {equals: "${userInput.station}"}}}}}
              ) {
                trainNumber
                timeTableRows(where: {station: {name: {equals: "${userInput.station}"}}}) {
                  scheduledTime
                }
              }
            }`,
        };
        fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept-Encoding": "gzip",
            },
            body: JSON.stringify(q1),
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then((result) => {
                console.log("result", result);
                schedule = new Date(
                    result.data.train[0].timeTableRows[0].scheduledTime,
                );
                schedule = schedule.toLocaleString("fi-FI", {
                    timeZone: "Europe/Helsinki",
                });
            });
    }

    onMount(getOptions);
</script>

<div class="main">
    <h1>Tehtävä 1</h1>
    <div class="userInput">
        <label for="id">valitse id</label>
        <select bind:value={userInput.id} type="Selection">
            {#if junat}
                {#each junat as juna}
                    <option value={juna}>{juna}</option>
                {/each}
            {/if}
        </select>
        <label for="station">Aseman nimi</label>
        <select bind:value={userInput.station}>
            {#if asemat}
                {#each Object.entries(asemat) as [code, name]}
                    <option value={code}>{name}</option>
                {/each}
            {/if}
        </select>
        <label for="date">Päivämäärä</label>
        <input bind:value={userInput.date} type="date" />
    </div>
    {#if userInput}
        <button on:click={fetchData}>Hae</button>
    {/if}
    {#if schedule && schedule.length > 0}
        <p>Juna on perillä valitulla asemalla: {schedule}</p>
    {/if}
</div>

<style>
    .main {
        margin: 3%;
    }
    .userInput {
        display: flex;
        flex-direction: column;
        margin-bottom: 20px;
        width: 15%;
    }
    tr,
    th,
    td {
        border: 1px solid black;
    }
</style>
