

async def fetch_db_constraints_and_metadata(resource_id: str) -> str:
    # Simulate fetching database constraints and metadata
    # In a real implementation, this would query the database
    """Fetch constraints and metadata of the database by connecting to it based on resource_id.
    Args:
        resource_id (str): ID of the database whose constraints and metadata are to be fetched.

    Returns:
        str: returns sample POSTGRESQL E-Commerce database schema with constraints and metadata.
    """
    print (f"Fetching constraints and metadata for input: {resource_id}")
    
    return """

        CREATE TABLE users (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            email VARCHAR(255) NOT NULL UNIQUE,
            password_hash VARCHAR(255) NOT NULL,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            phone VARCHAR(20),
            date_of_birth DATE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            is_active BOOLEAN DEFAULT TRUE,
            
            -- TABLE CONSTRAINTS
            CONSTRAINT chk_email_format CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'),
            CONSTRAINT chk_phone_format CHECK (phone IS NULL OR phone ~* '^\+?[1-9]\d{1,14}$'),
            CONSTRAINT chk_age CHECK (date_of_birth IS NULL OR date_of_birth <= CURRENT_DATE - INTERVAL '13 years'),
            CONSTRAINT chk_username_length CHECK (LENGTH(username) >= 3)
        );


        CREATE TABLE categories (
            category_id SERIAL PRIMARY KEY,
            category_name VARCHAR(100) NOT NULL UNIQUE,
            description TEXT,
            parent_category_id INTEGER,
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            
            -- FOREIGN KEY CONSTRAINT (Self-referencing)
            CONSTRAINT fk_parent_category FOREIGN KEY (parent_category_id) 
                REFERENCES categories(category_id) ON DELETE SET NULL
        );

        CREATE TABLE products (
            product_id SERIAL PRIMARY KEY,
            product_name VARCHAR(255) NOT NULL,
            description TEXT,
            price DECIMAL(10,2) NOT NULL,
            cost_price DECIMAL(10,2),
            sku VARCHAR(100) UNIQUE NOT NULL,
            category_id INTEGER NOT NULL,
            stock_quantity INTEGER DEFAULT 0,
            min_stock_level INTEGER DEFAULT 0,
            weight_kg DECIMAL(8,3),
            dimensions_cm VARCHAR(50), -- format: "LxWxH"
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            
            -- CONSTRAINTS
            CONSTRAINT fk_product_category FOREIGN KEY (category_id) 
                REFERENCES categories(category_id) ON DELETE RESTRICT,
            CONSTRAINT chk_price_positive CHECK (price > 0),
            CONSTRAINT chk_cost_price_positive CHECK (cost_price IS NULL OR cost_price >= 0),
            CONSTRAINT chk_stock_non_negative CHECK (stock_quantity >= 0),
            CONSTRAINT chk_min_stock_non_negative CHECK (min_stock_level >= 0),
            CONSTRAINT chk_weight_positive CHECK (weight_kg IS NULL OR weight_kg > 0),
            CONSTRAINT chk_sku_format CHECK (sku ~* '^[A-Z0-9-]+$')
        );


        CREATE TABLE orders (
            order_id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL,
            order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            status VARCHAR(20) DEFAULT 'pending',
            total_amount DECIMAL(12,2) NOT NULL,
            shipping_address TEXT NOT NULL,
            billing_address TEXT,
            payment_method VARCHAR(50),
            payment_status VARCHAR(20) DEFAULT 'pending',
            shipped_date TIMESTAMP,
            delivered_date TIMESTAMP,
            notes TEXT,
            
            -- CONSTRAINTS
            CONSTRAINT fk_order_user FOREIGN KEY (user_id) 
                REFERENCES users(user_id) ON DELETE CASCADE,
            CONSTRAINT chk_order_status CHECK (status IN ('pending', 'confirmed', 'processing', 'shipped', 'delivered', 'cancelled', 'refunded')),
            CONSTRAINT chk_payment_status CHECK (payment_status IN ('pending', 'completed', 'failed', 'refunded')),
            CONSTRAINT chk_total_amount_positive CHECK (total_amount > 0),
            CONSTRAINT chk_shipping_dates CHECK (shipped_date IS NULL OR shipped_date >= order_date),
            CONSTRAINT chk_delivery_dates CHECK (delivered_date IS NULL OR delivered_date >= COALESCE(shipped_date, order_date))
        );


        CREATE TABLE order_items (
            order_item_id SERIAL PRIMARY KEY,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            unit_price DECIMAL(10,2) NOT NULL,
            total_price DECIMAL(12,2) NOT NULL,
            
            -- CONSTRAINTS
            CONSTRAINT fk_order_item_order FOREIGN KEY (order_id) 
                REFERENCES orders(order_id) ON DELETE CASCADE,
            CONSTRAINT fk_order_item_product FOREIGN KEY (product_id) 
                REFERENCES products(product_id) ON DELETE RESTRICT,
            CONSTRAINT chk_quantity_positive CHECK (quantity > 0),
            CONSTRAINT chk_unit_price_positive CHECK (unit_price > 0),
            CONSTRAINT chk_total_price_calculation CHECK (total_price = quantity * unit_price),
            
            -- UNIQUE CONSTRAINT (Composite)
            CONSTRAINT uk_order_product UNIQUE (order_id, product_id)
        );


        CREATE TABLE reviews (
            review_id SERIAL PRIMARY KEY,
            product_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            rating INTEGER NOT NULL,
            review_text TEXT,
            review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            is_verified_purchase BOOLEAN DEFAULT FALSE,
            
            -- CONSTRAINTS
            CONSTRAINT fk_review_product FOREIGN KEY (product_id) 
                REFERENCES products(product_id) ON DELETE CASCADE,
            CONSTRAINT fk_review_user FOREIGN KEY (user_id) 
                REFERENCES users(user_id) ON DELETE CASCADE,
            CONSTRAINT chk_rating_range CHECK (rating >= 1 AND rating <= 5),
            
            -- UNIQUE CONSTRAINT (One review per user per product)
            CONSTRAINT uk_user_product_review UNIQUE (user_id, product_id)
        );



        CREATE INDEX idx_users_email ON users(email);
        CREATE INDEX idx_users_username ON users(username);
        CREATE INDEX idx_products_category ON products(category_id);
        CREATE INDEX idx_products_sku ON products(sku);
        CREATE INDEX idx_orders_user ON orders(user_id);
        CREATE INDEX idx_orders_date ON orders(order_date);
        CREATE INDEX idx_order_items_order ON order_items(order_id);
        CREATE INDEX idx_reviews_product ON reviews(product_id);


        CREATE INDEX idx_products_category_active ON products(category_id, is_active);
        CREATE INDEX idx_orders_user_status ON orders(user_id, status);
        CREATE INDEX idx_orders_date_status ON orders(order_date, status);

  
        CREATE INDEX idx_active_products ON products(product_name) WHERE is_active = TRUE;
        CREATE INDEX idx_pending_orders ON orders(order_date) WHERE status = 'pending';



        CREATE VIEW product_summary AS
        SELECT 
            p.product_id,
            p.product_name,
            p.price,
            p.stock_quantity,
            c.category_name,
            COALESCE(AVG(r.rating), 0) as avg_rating,
            COUNT(r.review_id) as review_count
        FROM products p
        LEFT JOIN categories c ON p.category_id = c.category_id
        LEFT JOIN reviews r ON p.product_id = r.product_id
        WHERE p.is_active = TRUE
        GROUP BY p.product_id, p.product_name, p.price, p.stock_quantity, c.category_name;

        CREATE VIEW order_summary AS
        SELECT 
            o.order_id,
            u.username,
            o.order_date,
            o.status,
            o.total_amount,
            COUNT(oi.order_item_id) as item_count
        FROM orders o
        JOIN users u ON o.user_id = u.user_id
        LEFT JOIN order_items oi ON o.order_id = oi.order_id
        GROUP BY o.order_id, u.username, o.order_date, o.status, o.total_amount;


        CREATE OR REPLACE FUNCTION update_updated_at_column()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.updated_at = CURRENT_TIMESTAMP;
            RETURN NEW;
        END;
        $$ language 'plpgsql';

        -- Triggers for automatic timestamp updates
        CREATE TRIGGER update_users_updated_at 
            BEFORE UPDATE ON users 
            FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

        CREATE TRIGGER update_products_updated_at 
            BEFORE UPDATE ON products 
            FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

        -- Function to validate stock before order
        CREATE OR REPLACE FUNCTION check_stock_availability()
        RETURNS TRIGGER AS $$
        BEGIN
            IF (SELECT stock_quantity FROM products WHERE product_id = NEW.product_id) < NEW.quantity THEN
                RAISE EXCEPTION 'Insufficient stock for product ID %', NEW.product_id;
            END IF;
            RETURN NEW;
        END;
        $$ LANGUAGE 'plpgsql';


        CREATE TRIGGER check_stock_before_order
            BEFORE INSERT ON order_items
            FOR EACH ROW EXECUTE FUNCTION check_stock_availability();


        CREATE OR REPLACE FUNCTION get_user_order_history(p_user_id INTEGER)
        RETURNS TABLE (
            order_id INTEGER,
            order_date TIMESTAMP,
            status VARCHAR(20),
            total_amount DECIMAL(12,2),
            item_count BIGINT
        ) AS $$
        BEGIN
            RETURN QUERY
            SELECT 
                o.order_id,
                o.order_date,
                o.status,
                o.total_amount,
                COUNT(oi.order_item_id) as item_count
            FROM orders o
            LEFT JOIN order_items oi ON o.order_id = oi.order_id
            WHERE o.user_id = p_user_id
            GROUP BY o.order_id, o.order_date, o.status, o.total_amount
            ORDER BY o.order_date DESC;
        END;
        $$ LANGUAGE 'plpgsql';


        CREATE SEQUENCE order_number_seq 
            START WITH 1000 
            INCREMENT BY 1 
            MINVALUE 1000 
            MAXVALUE 999999999 
            CYCLE;


        -- Custom domain for email validation
        CREATE DOMAIN email_type AS VARCHAR(255)
        CHECK (VALUE ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$');

        -- Custom domain for phone numbers
        CREATE DOMAIN phone_type AS VARCHAR(20)
        CHECK (VALUE IS NULL OR VALUE ~* '^\+?[1-9]\d{1,14}$');
"""