odoo.define('website_form_proposal.form', function (require) {
'use strict';

var core = require('web.core');
var FormEditorRegistry = require('website.form_editor_registry');
var rpc = require('web.rpc');

var _t = core._t;

FormEditorRegistry.add('create_proposal', {
    formFields: [{
        type: 'char',
        modelRequired: true,
        name: 'name',
        string: 'Title',
    }, {
        type: 'html',
        name: 'description',
        string: 'Description',
    }, {
        type: 'char',
        modelRequired: false,
        name: 'web_link',
        string: 'Url',
    }],
});

Promise.all([
    rpc.query({
        model: 'research.proposal.keyword.category',
        method: 'search_read',
        domain: [],
        fields: ['id', 'name'],
    }),
])
    .then(function (results) {
        var categories = results[0];

        var today = new Date();
        var expirationDate = new Date(today.getFullYear(), today.getMonth() + 3, today.getDate());

        var day = ("0" + expirationDate.getDate()).slice(-2);
        var month = ("0" + (expirationDate.getMonth() + 1)).slice(-2);
        var year = expirationDate.getFullYear();

        var formattedDate = day + "/" + month + "/" + year;

        var fields = [
            {
                type: 'date',
                modelRequired: false,
                value: formattedDate,
                name: 'expiration_date',
                string: 'Expiration Date',
            },
        ];

        categories.forEach(function (category) {
            fields.push({
                type: 'many2many',
                modelRequired: false,
                name: 'keywords',
                string: category.name,
                relation: 'research.proposal.keyword',
                domain: [['category', '=', category.id]],
            });
        });

        FormEditorRegistry.get('create_proposal').formFields = FormEditorRegistry.get('create_proposal').formFields.concat(fields);
    })
    .catch(function (error) {
        console.error(error);
    });
});