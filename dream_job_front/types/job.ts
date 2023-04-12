export type JobT = {
    id: number;
    category: number | null;
    description: string | null;
    title: string;
    company_name: string;
    company_location: string | null;
    company_email: string | null;
    position_salary: string;
    position_location: string;
    created_at_formatted: string;
}