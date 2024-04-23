<script>
    import { onMount } from "svelte";
    let osallistujat = [];
    let filteredOsallistujat = [];
    let kansallisuudet = [];
    let sarjat = [];
    let selected_country;
    let selected_sarja;

    onMount(async () => {
        try {
            const response = await fetch("http://localhost:5000/osallistujat/");
            osallistujat = await response.json();
            kansallisuudet = [
                ...new Set(
                    osallistujat.map((osallistuja) => osallistuja.kansallisuus),
                ),
            ];
            sarjat = [
                ...new Set(
                    osallistujat.map((osallistuja) => osallistuja.sarja),
                ),
            ];
            filteredOsallistujat = osallistujat;
        } catch (error) {
            console.error(error);
        }
    });

    $: console.log(osallistujat);
    $: console.log(filteredOsallistujat);
    $: console.log(selected_sarja);
    $: console.log(selected_country);

    let filter = () => {
        filteredOsallistujat = osallistujat;
        if (selected_country !== "") {
            filteredOsallistujat = filteredOsallistujat.filter(
                (osallistujat) =>
                    osallistujat.kansallisuus === selected_country,
            );
        }
        if (selected_sarja !== "") {
            filteredOsallistujat = filteredOsallistujat.filter(
                (osallistujat) => osallistujat.sarja === selected_sarja,
            );
        }
    };
</script>

<h1>Osallistujat</h1>

{#if osallistujat.length}
    <div class="napit">
        <select bind:value={selected_country} on:change={filter}>
            <option value="">Valitse kansallisuus</option>
            {#each kansallisuudet as kansallisuus}
                <option value={kansallisuus}>{kansallisuus}</option>
            {/each}
        </select>
        <select bind:value={selected_sarja} on:change={filter}>
            <option value="">Valitse sarja</option>
            {#each sarjat as sarja}
                <option value={sarja}>{sarja}</option>
            {/each}
        </select>
    </div>
    <table>
        <tr>
            <th>Kilpailijanumero</th>
            <th>Etunimi</th>
            <th>Sukunimi</th>
            <th>Kansallisuus</th>
            <th>Sarja</th>
        </tr>
        {#each filteredOsallistujat as osallistuja}
            <tr>
                <td>{osallistuja.id}</td>
                <td>{osallistuja.etunimi}</td>
                <td>{osallistuja.sukunimi}</td>
                <td>{osallistuja.kansallisuus}</td>
                <td>{osallistuja.sarja}</td>
            </tr>
        {/each}
    </table>
{/if}

<style>
    h1 {
        font-family: "Arial", sans-serif;
        text-align: center;
        color: black;
        border: 1px solid black;
        box-shadow: 5px 5px 15px black;
        background-color: moccasin;
    }
    table {
        border-collapse: collapse;
        background-color: goldenrod;
        box-shadow: 5px 5px 15px black;
        margin-left: 20%;
        margin-right: 20%;
        padding-top: 5%;
        padding-left: 20%;
        padding-bottom: 10%;
        width: 60%;
    }
    tr,
    th,
    td {
        border: 1px solid black;
    }
    tr:nth-child(even) {
        background-color: moccasin;
    }
    .napit {
        display: flex;
        justify-content: center;
        margin-top: 2%;
    }
</style>
