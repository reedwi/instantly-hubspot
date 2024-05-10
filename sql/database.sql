-- Create 'accounts' table
CREATE TABLE instantly_hubspot.accounts (
    id UUID PRIMARY KEY,
    portal_id BIGINT,
    hub_domain TEXT,
    install_user_email TEXT,
    install_user_id TEXT,
    install_date TIMESTAMPTZ,
    created_at TIMESTAMPTZ
);

-- Create 'subscriptions' table
CREATE TABLE instantly_hubspot.subscriptions (
    id UUID PRIMARY KEY,
    start_date TIMESTAMPTZ,
    end_date TIMESTAMPTZ,
    tier TEXT,
    created_at TIMESTAMPTZ
);

-- Create 'subscriptions_accounts' table
CREATE TABLE instantly_hubspot.subscriptions_accounts (
    subscription_id UUID REFERENCES instantly_hubspot.subscriptions(id),
    account_id UUID REFERENCES instantly_hubspot.accounts(id),
    created_at TIMESTAMPTZ,
    PRIMARY KEY (subscription_id, account_id)
);

-- Create 'payments' table
CREATE TABLE instantly_hubspot.payments (
    id UUID PRIMARY KEY,
    amount FLOAT,
    purchaser_email TEXT,
    portal_id BIGINT,
    created_at TIMESTAMPTZ
);

-- Create 'payments_subscriptions' table
CREATE TABLE instantly_hubspot.payments_subscriptions (
    payment_id UUID REFERENCES instantly_hubspot.payments(id),
    subscription_id UUID REFERENCES instantly_hubspot.subscriptions(id),
    created_at TIMESTAMPTZ,
    PRIMARY KEY (payment_id, subscription_id)
);

-- Create 'payments_accounts' table
CREATE TABLE instantly_hubspot.payments_accounts (
    payment_id UUID REFERENCES instantly_hubspot.payments(id),
    account_id UUID REFERENCES instantly_hubspot.accounts(id),
    created_at TIMESTAMPTZ,
    PRIMARY KEY (payment_id, account_id)
);

-- Create 'usage' table
CREATE TABLE instantly_hubspot.usage (
    id UUID PRIMARY KEY,
    account_id UUID REFERENCES instantly_hubspot.accounts(id),
    created_at TIMESTAMPTZ
);
