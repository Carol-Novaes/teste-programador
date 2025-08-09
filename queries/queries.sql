---------- 1. Exibir o nome e o email de todos os alunos ordenados alfabeticamente
SELECT 
    nome AS "Nome", 
    email AS "E-mail"
FROM 
    educacao_aluno 
ORDER BY 
    nome ASC;

---------- 2. Mostrar o nome e a nota de todos os alunos em uma atividade específica.
SELECT 
    a.nome AS "Aluno(a)", 
    d.nota AS "Nota", 
    ativ.nome AS "Atividade"
FROM 
    educacao_desempenho d
JOIN 
    educacao_aluno a ON d.aluno_id = a.codigo
JOIN 
    educacao_atividade ativ ON d.atividade_id = ativ.id 
WHERE ativ.id = 2         --- Alterar o id para mudar a atividade

---------- 3. Listar os nomes dos cursos que possuem disciplinas cadastradas.
SELECT 
    c.nome AS "Curso", 
    d.nome AS "Disciplina"
FROM 
    educacao_curso c
JOIN 
    educacao_disciplina d ON c.codigo = d.curso_id    

---------- 4. Exibir o nome dos alunos que não entregaram nenhuma atividade.     
SELECT 
    a.nome AS "Aluno(a)"
FROM 
    educacao_aluno a
WHERE 
    NOT EXISTS (
        SELECT 1 
        FROM educacao_desempenho d 
        WHERE d.aluno_id = a.codigo
    );

---------- 5. Exibir os nomes dos alunos que estão matriculados em disciplinas do curso de nome "Engenharia de Software".     
SELECT 
    a.nome AS "Aluno(a)", 
    d.nome AS "Disciplinas", 
    c.nome AS "Curso"
FROM 
    educacao_aluno a
JOIN 
    educacao_matricula m ON a.codigo = m.codigo_aluno_id
JOIN 
    educacao_disciplina d ON m.codigo_disciplina_id = d.codigo
JOIN 
    educacao_curso c ON d.curso_id = c.codigo
WHERE 
    c.nome = 'Engenharia de Software'

---------- 6. Exibir os alunos que têm média de desempenho acima de 8.0 em disciplinas do curso "Matemática".     
SELECT 
    a.nome AS "Aluno", 
    ROUND(AVG(d.nota), 2) AS "Média", 
    c.nome AS "Curso"
FROM 
    educacao_aluno a
JOIN 
    educacao_desempenho d ON a.codigo = d.aluno_id
JOIN 
    educacao_atividade ativ ON d.atividade_id = ativ.id
JOIN 
    educacao_disciplina disc ON ativ.disciplina_id = disc.codigo
JOIN 
    educacao_curso c ON disc.curso_id = c.codigo
WHERE 
    c.nome = 'Matemática'
GROUP BY 
    a.codigo, a.nome, c.nome
HAVING 
    AVG(d.nota) > 8.0

---------- 7. Listar todas as atividades realizadas no mês de maio de 2025.
SELECT 
    nome AS "Nome", 
    data_atividade "Data da Atividade"
FROM 
    educacao_atividade
WHERE 
    strftime('%Y-%m', data_atividade) = '2025-05'

---------- 8. Exibir a disciplina e a quantidade total de atividades cadastradas em cada uma.
SELECT 
    d.nome AS "Disciplina",
    COUNT(a.id) AS "Qntd. de Atividades"
FROM 
    educacao_disciplina d
LEFT JOIN 
    educacao_atividade a ON d.codigo = a.disciplina_id
GROUP BY 
    d.codigo, d.nome

---------- 9.Listar o nome de cada aluno e a média geral de suas notas em todas as atividades.     
SELECT 
    a.nome AS "Aluno(a)",
    AVG(n.nota) AS "Média de notas"
FROM 
    educacao_aluno a
LEFT JOIN 
    educacao_desempenho n ON a.codigo = n.aluno_id
GROUP BY 
    a.codigo, a.nome

---------- 10. Exibir os alunos que têm pelo menos uma nota abaixo de 5.0 em qualquer atividade.
SELECT
    a.nome AS "Aluno(a)",
    d.nome AS "Disciplina",
    t.nome AS "Atividade",
    e.nota AS "Nota"
FROM
    educacao_aluno a
JOIN
    educacao_desempenho e ON a.codigo = e.aluno_id
JOIN
    educacao_atividade t ON e.atividade_id = t.id
JOIN
    educacao_disciplina d ON t.disciplina_id = d.codigo
WHERE
    e.nota < 5.0