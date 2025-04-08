import i18n from '@/utils/i18n';

function validatePassword(password, appSettings) {
    const errors = [];

    if (!appSettings || typeof appSettings !== 'object') {
        console.error('Invalid appSettings provided');
        return [];
    }

    // Проверка длины пароля
    if (!(appSettings.min_length <= password.length && password.length <= appSettings.max_length)) {
        errors.push({
            code: "PASS-001",
            message: i18n.t('auth.error.password.PASS-001', { min: appSettings.min_length, max: appSettings.max_length })
        });
    }

    // Проверка наличия заглавных букв
    if (appSettings.require_uppercase && !/[A-Z]/.test(password)) {
        errors.push({
            code: "PASS-002",
            message: i18n.t('auth.error.password.PASS-002')
        });
    }

    // Проверка наличия строчных букв
    if (appSettings.require_lowercase && !/[a-z]/.test(password)) {
        errors.push({
            code: "PASS-003",
            message: i18n.t('auth.error.password.PASS-003')
        });
    }

    // Проверка наличия цифр
    if (appSettings.require_digit && !/\d/.test(password)) {
        errors.push({
            code: "PASS-004",
            message: i18n.t('auth.error.password.PASS-004')
        });
    }

    // Проверка наличия специальных символов
    if (appSettings.require_special_char) {
        const allowedSpecialCharsPattern = `[${appSettings.allowed_special_chars.replace(/[-/\\^$*+?.()|[\]{}]/g, '\\$&')}]`;
        const specialCharRegex = new RegExp(allowedSpecialCharsPattern);
        if (!specialCharRegex.test(password)) {
            errors.push({
                code: "PASS-005",
                message: i18n.t('auth.error.password.PASS-005', { allowed_chars: appSettings.allowed_special_chars })
            });
        }
    }

    return errors;
}




export default {
    validatePassword
}