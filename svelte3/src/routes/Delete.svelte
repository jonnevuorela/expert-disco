<script>
    import { onMount } from "svelte";
    let osallistujat = [];
    let selectedOsallistuja;

    onMount(async () => {
        try {
            const response = await fetch("http://localhost:5000/osallistujat/");
            osallistujat = await response.json();
        } catch (error) {
            console.error(error);
        }
    });

    function deleteOsallistuja() {
        fetch(`http://localhost:5000/osallistujat/${selectedOsallistuja}`, {
            method: "DELETE",
        })
            .then((response) => response.json())
            .then((json) => {
                console.log(json);
                selectedOsallistuja = null;
            });
    }

    $: console.log("selectedOsallistuja", selectedOsallistuja);
</script>

<h1>Poista kilpailija</h1>

<form>
    <div class="thing">
        <select bind:value={selectedOsallistuja}>
            {#each osallistujat as osallistuja}
                <option value={osallistuja.id}
                    >{osallistuja.etunimi} {osallistuja.sukunimi}</option
                >
            {/each}
        </select>
        {#if !selectedOsallistuja}
            <button>Valitse</button>
        {/if}
        {#if selectedOsallistuja}
            <div>
                <button on:click={deleteOsallistuja} class="deletebutton">
                    🗑️
                </button>
                <button on:click={() => (selectedOsallistuja = null)}>
                    Peruuta
                </button>
            </div>
        {/if}
    </div>
</form>

<style>
    h1 {
        font-family: "Arial", sans-serif;
        text-align: center;
        color: black;
        border: 1px solid black;
        box-shadow: 5px 5px 15px black;
        background-color: moccasin;
    }
    form {
        display: flex;
        flex-direction: column;

        justify-content: center;
        border-collapse: collapse;
        background-color: goldenrod;
        box-shadow: 5px 5px 15px black;
        margin-left: 20%;
        margin-right: 20%;
        padding-top: 5%;
        padding-left: 20%;
        padding-bottom: 10%;
        width: 40%;
    }
    .thing {
        display: flex;
        flex-direction: row;
    }
    .deletebutton {
        background-color: moccasin;
        border-radius: 0.2em;
        border-color: darkgray;
    }
    .deleteinput {
        background-color: moccasin;
        border-radius: 0.2em;
        width: 20%;
    }
</style>
