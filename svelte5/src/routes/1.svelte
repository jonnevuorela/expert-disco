<script>
    import { onMount } from "svelte";
    import Home from "./Home.svelte";
    const url = "https://rata.digitraffic.fi/api/v2/graphql/graphql";
    let schedule;
    let junat;
    let asemat = { nimi: "", lyhenne: "" };
    let userInput = { id: "", station: "", date: "" };
    //$: console.log(trains)
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
                        acc[item.stationShortCode] = item.stationName;
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
              train(trainNumber: ${userInput.id}, departureDate: "${userInput.date}") {
                timeTableRows {
                  station {
                    name
                  }
                  scheduledTime
                }
              }
            }`,
        };
        console.log(q1.query);
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
                schedule = result.data.train[0].timeTableRows;
                console.log("schedule", schedule);
                schedule = schedule.filter(
                    (value) => value.station.name === userInput.station,
                );
                console.log("filtered schedule", schedule);
            });
    }
    onMount(getOptions);
    $: console.log("id", userInput.id);
    $: console.log("date", userInput.date);
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
                    <option value={code}>{name} ({code})</option>
                {/each}
            {/if}
        </select>
        <label for="date">Päivämäärä</label>
        <input bind:value={userInput.date} type="date" />
    </div>
    {#if userInput}
        <p>Valittu juna: {userInput.id}</p>
        <p>Valittu asema: {userInput.station}</p>
        <p>Valittu päivämäärä: {userInput.date}</p>
        <button on:click={fetchData}>Hae</button>
    {/if}
    {#if schedule && schedule.length > 0}
        <table>
            <tr>
                <th>Train number</th>
                <th>DepartureDate</th>
                <th>Time</th>
                <th>Location</th>
            </tr>
            {#each schedule as s}
                <tr>
                    <td>{s.trainNumber}</td>
                    <td>{s.departureDate}</td>
                    {#if s.trainLocations}
                        <td
                            >{s.trainLocations[0].timestamp.getHours()}:{s.trainLocations[0].timestamp.getMinutes()}</td
                        >
                        <td>{s.trainLocations[0].location}</td>
                    {/if}
                </tr>
            {/each}
        </table>
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
