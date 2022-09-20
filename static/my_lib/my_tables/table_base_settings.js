const general_table_settings = {
    classes: 'table table-bordered table-hover table-striped table-sm',
    sortReset: true, // Set true to reset the sort on third click.
    search: true,

    filterControl: true,

    showExport: true,
    exportTypes: ['json', 'csv', 'excel','xlsx', 'doc', 'pdf'],

    buttonsClass: 'table_buttons',

    searchAccentNeutralise: true,
    showButtonIcons: true,
    showColumnsToggleAll: true, //Set true to show a toggle all checkbox within the columns option/dropdown.
    showExtendedPagination: true,
    showRefresh: true,
    showButtonText: false,
    clickToSelect: true,
    pagination: true,
    visibleSearch: true,
    paginationDetailHAlign: 'right',
    paginationVAlign: 'both',
    paginationPreText: 'Previous',
    paginationNextText: 'Next',
    pageList: [25, 50, 100, 'all'],
    undefinedText: 'N/A',
};

function dateTimeFormatter(value) {
    if (value) {
        return moment(value).format('YYYY MMMM DD'); //, hh:mm A
    } else {
        return null;
    }
}


function monthFormatter(value) {
    if (value) {
        return (new Date(value)).toLocaleString('default', {month: 'long'});
    } else {
        return null;
    }

}

function yearFormatter(value) {
    if (value) {
        return new Date(value).getUTCFullYear();
    } else {
        return null;
    }
}


function editFormatter(value) {
    return `<a href="${value}" class="entry_edit_button" target="_blank" rel="noopener noreferrer">
<svg width="25px" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><!--! Font Awesome Pro 6.1.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M160 32V64H288V32C288 14.33 302.3 0 320 0C337.7 0 352 14.33 352 32V64H400C426.5 64 448 85.49 448 112V160H0V112C0 85.49 21.49 64 48 64H96V32C96 14.33 110.3 0 128 0C145.7 0 160 14.33 160 32zM0 192H448V235.6L289.3 394.3C281.1 402.5 275.3 412.8 272.5 424.1L257.4 484.2C255.1 493.6 255.7 503.2 258.8 512H48C21.49 512 0 490.5 0 464V192zM120 272C106.7 272 96 282.7 96 296C96 309.3 106.7 320 120 320H264C277.3 320 288 309.3 288 296C288 282.7 277.3 272 264 272H120zM120 416H200C213.3 416 224 405.3 224 392C224 378.7 213.3 368 200 368H120C106.7 368 96 378.7 96 392C96 405.3 106.7 416 120 416zM564.1 250.1C579.8 265.7 579.8 291 564.1 306.7L534.7 336.1L463.8 265.1L493.2 235.7C508.8 220.1 534.1 220.1 549.8 235.7L564.1 250.1zM311.9 416.1L441.1 287.8L512.1 358.7L382.9 487.9C378.8 492 373.6 494.9 368 496.3L307.9 511.4C302.4 512.7 296.7 511.1 292.7 507.2C288.7 503.2 287.1 497.4 288.5 491.1L303.5 431.8C304.9 426.2 307.8 421.1 311.9 416.1V416.1z"/></svg>
</a>`
}


function deleteFormatter(value) {
    return `<a href="${value}" class="entry_delete_button" target="_blank" rel="noopener noreferrer">
<svg width="20px" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Pro 6.1.1 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2022 Fonticons, Inc. --><path d="M135.2 17.69C140.6 6.848 151.7 0 163.8 0H284.2C296.3 0 307.4 6.848 312.8 17.69L320 32H416C433.7 32 448 46.33 448 64C448 81.67 433.7 96 416 96H32C14.33 96 0 81.67 0 64C0 46.33 14.33 32 32 32H128L135.2 17.69zM31.1 128H416V448C416 483.3 387.3 512 352 512H95.1C60.65 512 31.1 483.3 31.1 448V128zM111.1 208V432C111.1 440.8 119.2 448 127.1 448C136.8 448 143.1 440.8 143.1 432V208C143.1 199.2 136.8 192 127.1 192C119.2 192 111.1 199.2 111.1 208zM207.1 208V432C207.1 440.8 215.2 448 223.1 448C232.8 448 240 440.8 240 432V208C240 199.2 232.8 192 223.1 192C215.2 192 207.1 199.2 207.1 208zM304 208V432C304 440.8 311.2 448 320 448C328.8 448 336 440.8 336 432V208C336 199.2 328.8 192 320 192C311.2 192 304 199.2 304 208z"/></svg>
</i></a>`
}


function rowContentFormatter(index, row, element) {
    element.html(`<strong>Details:</strong><br>${row['incident_details']}`);
}

function init_piracy_table() {
    let column_headers = [
        {field: 'culprit_vessel_entity', title: "Culprit Vessel (MMSI)", sortable: true, filterControl: 'input',},
        {field: 'victim_vessel_entity', title: "Victim Vessel (MMSI)", sortable: true, filterControl: 'input',},
        {field: 'type_of_incident', title: "Incident Type", sortable: true, filterControl: 'select',},
        {field: 'location_lat', title: "Lat", sortable: true,},
        {field: 'location_lon', title: "Lon", sortable: true,},
        {field: 'country_name', title: "Country", sortable: true, filterControl: 'select',},
        {field: 'sub_region', title: "Sub Region", sortable: true, filterControl: 'select',},
        {field: 'incidence_datetime', title: "Date", sortable: true, formatter: dateTimeFormatter,},
        {field: 'month', title: "Month", sortable: true, formatter: monthFormatter, filterControl: 'select',},
        {field: 'year', title: "Year", sortable: true, formatter: yearFormatter, filterControl: 'select',},

        {field: 'edit_url', title: "Edit", sortable: true, formatter: editFormatter, align: 'center'},
        {field: 'delete_url', title: "Delete", sortable: true, formatter: deleteFormatter, align: 'center'},
    ];

    let table_el = $('#piracy_table');

    let table_table_committees_and_executives_settings = {
        columns: column_headers,
        detailView: true,
        detailFormatter: rowContentFormatter,
    };

    table_el.bootstrapTable(
        Object.assign({}, general_table_settings, table_table_committees_and_executives_settings)
    )
}

function init_iuu_table() {
    let column_headers = [
        {field: 'culprit_vessel_entity', title: "Culprit Vessel (MMSI)", sortable: true, filterControl: 'input',},
        {field: 'type_of_incident', title: "Incident Type", sortable: true, filterControl: 'select',},
        {field: 'country_name', title: "Country", sortable: true, filterControl: 'select',},
        {field: 'sub_region', title: "Sub Region", sortable: true, filterControl: 'select',},
        {field: 'incidence_datetime', title: "Date", sortable: true, formatter: dateTimeFormatter,},
        {field: 'month', title: "Month", sortable: true, formatter: monthFormatter, filterControl: 'select',},
        {field: 'year', title: "Year", sortable: true, formatter: yearFormatter, filterControl: 'select',},
        {field: 'edit_url', title: "Edit", sortable: true, formatter: editFormatter, align: 'center'},
        {field: 'delete_url', title: "Delete", sortable: true, formatter: deleteFormatter, align: 'center'},
    ];

    let table_el = $('#iuu_table');

    let table_table_committees_and_executives_settings = {
        columns: column_headers,
        detailView: true,
        detailFormatter: rowContentFormatter,
    };

    table_el.bootstrapTable(
        Object.assign({}, general_table_settings, table_table_committees_and_executives_settings)
    )
}

function init_drug_trafficking_table() {
    let column_headers = [
        {field: 'culprit_vessel_entity', title: "Culprit Vessel (MMSI)", sortable: true, filterControl: 'input',},
        {
            field: 'multiple_vessels_involved',
            title: "Multiple Vessels Involved",
            sortable: true,
            filterControl: 'select',
        },
        {field: 'type_of_drug', title: "Drug Type", sortable: true, filterControl: 'select',},
        {field: 'total_tonnage_seized', title: "Tonnage Seized", sortable: true, filterControl: 'input',},
        {field: 'country_name', title: "Country", sortable: true, filterControl: 'select',},
        {field: 'sub_region', title: "Sub Region", sortable: true, filterControl: 'select',},
        {field: 'incidence_datetime', title: "Date", sortable: true, formatter: dateTimeFormatter,},
        {field: 'month', title: "Month", sortable: true, formatter: monthFormatter, filterControl: 'select',},
        {field: 'year', title: "Year", sortable: true, formatter: yearFormatter, filterControl: 'select',},
        {field: 'edit_url', title: "Edit", sortable: true, formatter: editFormatter, align: 'center'},
        {field: 'delete_url', title: "Delete", sortable: true, formatter: deleteFormatter, align: 'center'},
    ];

    let table_el = $('#drug_trafficking_table');

    let table_table_committees_and_executives_settings = {
        columns: column_headers,
        detailView: true,
        detailFormatter: rowContentFormatter,
    };

    table_el.bootstrapTable(
        Object.assign({}, general_table_settings, table_table_committees_and_executives_settings)
    )
}

function init_ship_to_ship_table() {
    let column_headers = [
        {field: 'type_of_vessel', title: "Vessel Type", sortable: true, filterControl: 'select',},
        {field: 'country_name', title: "Country", sortable: true, filterControl: 'select',},
        {field: 'sub_region', title: "Sub Region", sortable: true, filterControl: 'select',},
        {field: 'incidence_datetime', title: "Date", sortable: true, formatter: dateTimeFormatter,},
        {field: 'month', title: "Month", sortable: true, formatter: monthFormatter, filterControl: 'select',},
        {field: 'year', title: "Year", sortable: true, formatter: yearFormatter, filterControl: 'select',},
        {field: 'edit_url', title: "Edit", sortable: true, formatter: editFormatter, align: 'center'},
        {field: 'delete_url', title: "Delete", sortable: true, formatter: deleteFormatter, align: 'center'},
    ];

    let table_el = $('#ship_to_ship_table');

    let table_table_committees_and_executives_settings = {
        columns: column_headers,
        detailView: true,
        detailFormatter: rowContentFormatter,
    };

    table_el.bootstrapTable(
        Object.assign({}, general_table_settings, table_table_committees_and_executives_settings)
    )
}

function init_stow_away_table() {
    let column_headers = [
        {field: 'incident_category', title: "Incident Category", sortable: true, filterControl: 'select',},
        {field: 'source_port', title: "Source Port", sortable: true, filterControl: 'input',},
        {field: 'destination_port', title: "Destination Port", sortable: true, filterControl: 'input',},
        {field: 'no_individuals_involved', title: "Individuals Involved", sortable: true, filterControl: 'input',},
        {field: 'country_name', title: "Country", sortable: true, filterControl: 'select',},
        {field: 'sub_region', title: "Sub Region", sortable: true, filterControl: 'select',},
        {field: 'incidence_datetime', title: "Date", sortable: true, formatter: dateTimeFormatter,},
        {field: 'month', title: "Month", sortable: true, formatter: monthFormatter, filterControl: 'select',},
        {field: 'year', title: "Year", sortable: true, formatter: yearFormatter, filterControl: 'select',},
        {field: 'edit_url', title: "Edit", sortable: true, formatter: editFormatter, align: 'center'},
        {field: 'delete_url', title: "Delete", sortable: true, formatter: deleteFormatter, align: 'center'},
    ];

    let table_el = $('#stow_away_table');

    let table_table_committees_and_executives_settings = {
        columns: column_headers,
        detailView: true,
        detailFormatter: rowContentFormatter,
    };

    table_el.bootstrapTable(
        Object.assign({}, general_table_settings, table_table_committees_and_executives_settings)
    )
}

function init_maritime_accidents_table() {
    let column_headers = [
        {field: 'accident_category', title: "Accident Category", sortable: true, filterControl: 'select',},
        {field: 'country_name', title: "Country", sortable: true, filterControl: 'select',},
        {field: 'sub_region', title: "Sub Region", sortable: true, filterControl: 'select',},
        {field: 'incidence_datetime', title: "Date", sortable: true, formatter: dateTimeFormatter,},
        {field: 'month', title: "Month", sortable: true, formatter: monthFormatter, filterControl: 'select',},
        {field: 'year', title: "Year", sortable: true, formatter: yearFormatter, filterControl: 'select',},
        {field: 'edit_url', title: "Edit", sortable: true, formatter: editFormatter, align: 'center'},
        {field: 'delete_url', title: "Delete", sortable: true, formatter: deleteFormatter, align: 'center'},
    ];

    let table_el = $('#maritime_accidents_table');

    let table_table_committees_and_executives_settings = {
        columns: column_headers,
        detailView: true,
        detailFormatter: rowContentFormatter,
    };

    table_el.bootstrapTable(
        Object.assign({}, general_table_settings, table_table_committees_and_executives_settings)
    )
}
