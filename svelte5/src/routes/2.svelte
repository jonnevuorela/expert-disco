<script>
    import { onMount } from "svelte";

    const url = "https://rata.digitraffic.fi/api/v2/graphql/graphql";
    let junat;
    let foo;
    let bar;
    let inputId;
    let haetaan = false;

    function getOptions() {
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
        getJunat();
    }
    async function fetchEstimate() {
        let today = new Date();
        let date = today.toISOString().slice(0, 10);

        let start = new Date();
        let stop = new Date();
        let result = null;

        // query while loopissa kunnes saadaan tyydyttävä vastaus
        // aikaikkunaa laajennetaan joka iteraatiossa
        // ei ehkä tehokkain tapa jos juna ei kulje
        // puuttuu myös aikakatkaisu
        while (!result || !result.data.train[0].timeTableRows) {
            haetaan = true;
            start.setMinutes(start.getMinutes());
            stop.setMinutes(stop.getMinutes() + 10);

            let formattedStart = start.toISOString();
            let formattedStop = stop.toISOString();

            console.log("start", formattedStart);
            console.log("stop", formattedStop);

            const q1 = {
                query: `{
                train(trainNumber: ${inputId}, departureDate: "${date}") {
                   timeTableRows(
                    where: {
                      and: [
                        { scheduledTime: { greaterThan: "${formattedStart}" } },
                        { scheduledTime: { lessThan: "${formattedStop}" } }
                      ]
                    }
                  ) {
                    differenceInMinutes
                    scheduledTime
                    station{name}
                  }

                }}`,
            };

            result = await fetchBar(q1);
        }

        foo = result.data.train[0].timeTableRows;
        console.log("foo", foo);
        bar = {
            aika: foo[0].scheduledTime,
            paikka: foo[0].station.name,
            ero: foo[0].differenceInMinutes,
        };
        haetaan = false;
    }

    async function fetchBar(query) {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept-Encoding": "gzip",
            },
            body: JSON.stringify(query),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        return await response.json();
    }
    onMount(getOptions);
</script>

<div class="main">
    <h1>Tehtävä2</h1>
    tämä hakee ennemminkin seuraavan aseman eikä live sijaintia<br />
    <select bind:value={inputId}>
        {#if junat}
            {#each junat as juna}
                <option value={juna}>{juna}</option>
            {/each}
        {/if}
    </select>
    <button on:click={fetchEstimate}>Hae</button>
    {#if haetaan}
        <p>Haetaan...</p>
    {/if}
    {#if foo}
        <p>
            {Math.floor(-((new Date() - new Date(bar.aika)) / 60000)) < 1
                ? "alle"
                : Math.floor(-((new Date() - new Date(bar.aika)) / 60000))}
            minuutin päästä kohteessa {bar.paikka}
        </p>
        {#if bar.ero}
            <p>{bar.ero} minuuttia myöhässä</p>
        {:else}
            <p>Juna on aikataulussa</p>
        {/if}
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
