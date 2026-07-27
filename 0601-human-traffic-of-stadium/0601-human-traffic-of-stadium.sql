SELECT DISTINCT
    id,
    visit_date,
    people
FROM
(
    -- First person in the sequence
    SELECT
        s.id,
        s.visit_date,
        s.people
    FROM Stadium s
    JOIN Stadium st
        ON s.id + 1 = st.id
    JOIN Stadium sta
        ON st.id + 1 = sta.id
    WHERE s.people >= 100
      AND st.people >= 100
      AND sta.people >= 100

    UNION

    -- Second person in the sequence
    SELECT
        st.id,
        st.visit_date,
        st.people
    FROM Stadium s
    JOIN Stadium st
        ON s.id + 1 = st.id
    JOIN Stadium sta
        ON st.id + 1 = sta.id
    WHERE s.people >= 100
      AND st.people >= 100
      AND sta.people >= 100

    UNION

    -- Third person in the sequence
    SELECT
        sta.id,
        sta.visit_date,
        sta.people
    FROM Stadium s
    JOIN Stadium st
        ON s.id + 1 = st.id
    JOIN Stadium sta
        ON st.id + 1 = sta.id
    WHERE s.people >= 100
      AND st.people >= 100
      AND sta.people >= 100
) t
ORDER BY id;