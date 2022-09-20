$(document).ready(function () {
    const app = Vue.createApp({
        data() {
            return {
                leftDrawerOpen: true,
                dash_section: [
                    {icon: 'sports_kabaddi', label: 'Piracy', model_name:'Piracy', color: 'teal'},
                    {icon: 'fmd_bad', label: 'IUU', model_name:'IUU', color: 'teal'},
                    {icon: 'handshake', label: 'Drug Trafficking', model_name:'DrugTrafficking', color: 'teal'},
                    {icon: 'directions_boat', label: 'Ship To Ship', model_name:'ShipToShip', color: 'teal'},
                    {icon: 'kayaking', label: 'Illegal Migrations', model_name:'IllegalMigrations', color: 'teal'},
                    {icon: 'personal_injury', label: 'Maritime Accidents', model_name:'MaritimeAccidents', color: 'teal'},
                    ],
                current_section:'Piracy',
                sections:{
                    Piracy: {show:false},
                    IUU: {show:false},
                    DrugTrafficking: {show:false},
                    ShipToShip: {show:false},
                    IllegalMigrations: {show:false},
                    MaritimeAccidents: {show:false},
                }
            };
        },
        methods: {
            toggleLeftDrawer() {
                this.leftDrawerOpen = !this.leftDrawerOpen;
            },
            showSection(subsection) {
                this.sections[subsection].show = true;
                this.current_section = subsection;
                // TODO set cookies for selected subsection
                for (let key of Object.keys(this.sections)) {
                    if (key !== subsection) {
                        this.sections[key].show = false;
                    }
                }
            }
        },
        mounted: function () {
            this.sections[this.current_section].show = true;
        },
        watch: {
            'sections.Piracy.show'(newValue) {
                if (newValue === true) {
                    init_piracy_table();
                }
            },
            'sections.IUU.show'(newValue) {
                if (newValue === true) {
                    init_iuu_table();
                }
            },
            'sections.DrugTrafficking.show'(newValue) {
                if (newValue === true) {
                    init_drug_trafficking_table();
                }
            },
            'sections.ShipToShip.show'(newValue) {
                if (newValue === true) {
                    init_ship_to_ship_table();
                }
            },
            'sections.IllegalMigrations.show'(newValue) {
                if (newValue === true) {
                    init_stow_away_table();
                }
            },
            'sections.MaritimeAccidents.show'(newValue) {
                if (newValue === true) {
                    init_maritime_accidents_table();
                }
            },
        }
    });

    app.use(Quasar);
    app.mount('#vue_dashboard')
});
