const mask = {
    cpf (value) {
        return value
            .replace(/\D/g, '')
            .replace(/(\d{3})(\d)/, '$1.$2')
            .replace(/(\d{3})(\d)/, '$1.$2')
            .replace(/(\d{3})(\d)/, '$1-$2');

    },

    age (value) {
        return value
            .replace(/\D/g, '');

    },

    name (value) {
        return value
            .replace(/\d/g, '')
    }

}