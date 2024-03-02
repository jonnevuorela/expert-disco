<script>
    import CustomersTable from './CustomersTable.svelte'
    import {allCustomers} from '../lib/customers'
    import FilterCustomers from './FilterCustomers.svelte';

    let customers = allCustomers

</script>

<CustomersTable customers={customers}/>
<FilterCustomers bind:customers={customers} allCustomers={allCustomers}/>