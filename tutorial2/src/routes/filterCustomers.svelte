<script>
    export let customers;
    export let allCustomers;
    let countries = ["US", "UK", "Finland"];
    let selected_country = "",
        active = true,
        interested = true,
        passive = true;

    let age = "all";

    function myFilter() {
        console.log(selected_country);
        customers = allCustomers;
        if (selected_country != "") {
            customers = customers.filter(
                (customer) => customer.country == selected_country,
            );
        }
        console.log(customers);
        if (!active) {
            customers = customers.filter(
                (customer) => customer.status != "active",
            );
            console.log(customers);
        }
        if (!passive) {
            customers = customers.filter(
                (customer) => customer.status != "passive",
            );
        }
        if (!interested) {
            customers = customers.filter(
                (customer) => customer.status != "interested",
            );
        }
        if (age != "all") {
            customers = customers.filter(
                (customer) => customer.agegroup == age,
            );
        }
    }
</script>

<h4>Choose which customers to show</h4>
<div>
    <select bind:value={selected_country} on:change={myFilter}>
        <option value="">Filter by country</option>
        {#each countries as country}
            <option value={country}>{country}</option>
        {/each}
    </select>
</div>

<div>
    <label
        ><input type="checkbox" bind:checked={active} on:change={myFilter} />
        Active
    </label>

    <label
        ><input
            type="checkbox"
            bind:checked={interested}
            on:change={myFilter}
        />
        Interested
    </label>

    <label>
        <input type="checkbox" bind:checked={passive} on:change={myFilter} />
        Passive
    </label>
</div>

<div>
    <label
        ><input
            type="radio"
            name="age"
            value="young"
            bind:group={age}
            on:change={myFilter}
        />
        Young
    </label>

    <label
        ><input
            type="radio"
            name="age"
            value="adult"
            bind:group={age}
            on:change={myFilter}
        />
        Adult
    </label>

    <label
        ><input
            type="radio"
            name="age"
            value="all"
            bind:group={age}
            on:change={myFilter}
        />
        All
    </label>
</div>
