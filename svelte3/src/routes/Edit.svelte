<script>
    import { onMount } from "svelte";
    let osallistujat = [];
    let selectedOsallistuja;
    let editOsallistuja;
    let editing = {
        etunimi: "",
        sukunimi: "",
        sarja: "",
        numero: "",
        kansallisuus: "",
    };
    let edit = {
        etunimi: false,
        sukunimi: false,
        sarja: false,
        numero: false,
        kansallisuus: false,
    };
    let edited = {
        etunimi: "",
        sukunimi: "",
        sarja: "",
        id: "",
        kansallisuus: "",
    };

    onMount(async () => {
        try {
            const response = await fetch("http://localhost:5000/osallistujat/");
            osallistujat = await response.json();
        } catch (error) {
            console.error(error);
        }
    });

    function showForm() {
        fetch(`http://localhost:5000/osallistujat/${selectedOsallistuja.id}`)
            .then((response) => response.json())
            .then((json) => (editOsallistuja = json));
    }

    async function save() {
        if (!edited.etunimi) edited.etunimi = selectedOsallistuja.etunimi;
        if (!edited.sukunimi) edited.sukunimi = selectedOsallistuja.sukunimi;
        if (!edited.id) edited.id = selectedOsallistuja.id;
        if (!edited.sarja) edited.sarja = selectedOsallistuja.sarja;
        if (!edited.kansallisuus)
            edited.kansallisuus = selectedOsallistuja.kansallisuus;
        fetch(`http://localhost:5000/osallistujat/${selectedOsallistuja.id}`, {
            method: "PATCH",
            body: JSON.stringify(edited),
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((response) => response.json())
            .then((json) => {
                console.log(json);
                editOsallistuja = null;
                alert(
                    `Osallistujaa \"${selectedOsallistuja.etunimi} ${selectedOsallistuja.sukunimi}\" muokattu`,
                );
                window.location.reload();
            });
    }
    $: console.log("selectedOsallistuja", selectedOsallistuja);
    $: console.log("edited", edited);
</script>

<h1>Valitse muokattava osallistuja</h1>

<form>
    <div>
        <select bind:value={selectedOsallistuja}>
            <option value="">Valitse osallistuja</option>
            {#each osallistujat as osallistuja}
                <option value={osallistuja}
                    >{osallistuja.etunimi} {osallistuja.sukunimi}</option
                >
            {/each}
        </select>
        <button on:click={showForm}>Valitse</button>
    </div>
    <div class="editform">
        {#if editOsallistuja}
            <div id="etunimi">
                Nimi:
                {#if !edit.etunimi}
                    {#if !edited.etunimi}
                        {selectedOsallistuja.etunimi}
                    {/if}
                    {#if edited.etunimi}
                        {edited.etunimi}
                    {/if}
                    <button
                        on:click={() => (edit.etunimi = !edit.etunimi)}
                        class="editbutton"
                    >
                        ✏️
                    </button>
                {/if}
                {#if edit.etunimi}
                    <input
                        class="editinput"
                        type="text"
                        placeholder={selectedOsallistuja.etunimi}
                        bind:value={editing.etunimi}
                    />
                    <button on:click={() => (edit.etunimi = !edit.etunimi)}
                        >🚫</button
                    >
                    <button
                        on:click={(edited.etunimi = editing.etunimi)}
                        on:click={() => (edit.etunimi = !edit.etunimi)}
                        >💾</button
                    >
                {/if}
            </div>
            <div id="sukunimi">
                Sukunimi:
                {#if !edit.sukunimi}
                    {#if !edited.sukunimi}
                        {selectedOsallistuja.sukunimi}
                    {/if}
                    {#if edited.sukunimi}
                        {edited.sukunimi}
                    {/if}
                    <button
                        on:click={() => (edit.sukunimi = !edit.sukunimi)}
                        class="editbutton"
                    >
                        ✏️
                    </button>
                {/if}
                {#if edit.sukunimi}
                    <input
                        class="editinput"
                        type="text"
                        placeholder={selectedOsallistuja.sukunimi}
                        bind:value={editing.sukunimi}
                    />
                    <button on:click={() => (edit.sukunimi = !edit.sukunimi)}
                        >🚫</button
                    >
                    <button
                        on:click={(edited.sukunimi = editing.sukunimi)}
                        on:click={() => (edit.sukunimi = !edit.sukunimi)}
                        >💾</button
                    >
                {/if}
            </div>
            <div id="numero">
                Numero:
                {#if !edit.numero}
                    {#if !edited.id}
                        {selectedOsallistuja.id}
                    {/if}
                    {#if edited.id}
                        {edited.id}
                    {/if}

                    <button
                        on:click={() => (edit.numero = !edit.numero)}
                        class="editbutton"
                    >
                        ✏️
                    </button>
                {/if}
                {#if edit.numero}
                    <input
                        class="editinput"
                        type="text"
                        placeholder={selectedOsallistuja.id}
                        bind:value={editing.numero}
                    />
                    <button on:click={() => (edit.numero = !edit.numero)}
                        >🚫</button
                    >
                    <button
                        on:click={(edited.id = editing.numero)}
                        on:click={() => (edit.numero = !edit.numero)}>💾</button
                    >
                {/if}
            </div>
            <div id="sarja">
                Sarja:
                {#if !edit.sarja}
                    {#if !edited.sarja}
                        {selectedOsallistuja.sarja}
                    {/if}
                    {#if edited.sarja}
                        {edited.sarja}
                    {/if}
                    <button
                        on:click={() => (edit.sarja = !edit.sarja)}
                        class="editbutton"
                    >
                        ✏️
                    </button>
                {/if}
                {#if edit.sarja}
                    <input
                        class="editinput"
                        type="text"
                        placeholder={selectedOsallistuja.sarja}
                        bind:value={editing.sarja}
                    />
                    <button on:click={() => (edit.sarja = !edit.sarja)}
                        >🚫</button
                    >
                    <button
                        on:click={(edited.sarja = editing.sarja)}
                        on:click={() => (edit.sarja = !edit.sarja)}>💾</button
                    >
                {/if}
            </div>
            <div id="kansallisuus">
                Kansallisuus:
                {#if !edit.kansallisuus}
                    {#if !edited.kansallisuus}
                        {selectedOsallistuja.kansallisuus}
                    {/if}
                    {#if edited.kansallisuus}
                        {edited.kansallisuus}
                    {/if}
                    <button
                        on:click={() =>
                            (edit.kansallisuus = !edit.kansallisuus)}
                        class="editbutton"
                    >
                        ✏️
                    </button>
                {/if}
                {#if edit.kansallisuus}
                    <input
                        class="editinput"
                        type="text"
                        placeholder={selectedOsallistuja.kansallisuus}
                        bind:value={editing.kansallisuus}
                    />
                    <button
                        on:click={() =>
                            (edit.kansallisuus = !edit.kansallisuus)}>🚫</button
                    >
                    <button
                        on:click={(edited.kansallisuus = editing.kansallisuus)}
                        on:click={() =>
                            (edit.kansallisuus = !edit.kansallisuus)}>💾</button
                    >
                {/if}
            </div>
            <button type="submit" on:click={save}> Tallenna </button>
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
    .editbutton {
        background: none;
        border: none;
    }
    .editinput {
        background-color: moccasin;
        border-radius: 0.2em;
        width: 20%;
    }
</style>
