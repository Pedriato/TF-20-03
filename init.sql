CREATE TABLE alunos (
    aluno_id VARCHAR(5) NOT NULL,
    nome VARCHAR(40) NOT NULL,
    endereco VARCHAR(60),
    cidade VARCHAR(15),
    estado VARCHAR(15),
    cep VARCHAR(10),
    pais VARCHAR(15),
    telefone VARCHAR(24)

    
);

INSERT INTO alunos (aluno_id, nome, endereco, cidade, estado, cep, pais, telefone) VALUES
('A001', 'João Silva', 'Rua A', 'Atibaia', 'SP', '01234-567', 'Brasil', 11111111111'),
('A002', 'Maria Souza', 'Rua B', 'Pinheiral', 'RJ', '98765-432', 'Brasil', '222222222222'),
('A003', 'Carlos Lima', 'Rua C', 'Lençois', 'BA', '45678-901', 'Brasil', '33333333333'),
('A004', 'Ana Oliveira', 'Rua D', 'Juiz de Fora', 'MG', '23456-789', 'Brasil', '44444444444'),
('A005', 'Pedro Santos', 'Rua E', 'Curitiba', 'PR', '34567-890', 'Brasil', '55555555555'),
('A006', 'Fernanda Costa', 'Rua F', 'Fortaleza', 'CE', '45678-901', 'Brasil', '66666666666'),
('A007', 'Rafael Almeida', 'Rua G', 'Manaus', 'AM', '12345-678', 'Brasil', '77777777777'),
('A008', 'Juliana Campos', 'Rua H', 'Recife', 'PE', '54321-098', 'Brasil', '88888888888'),
('A009', 'Gustavo Dias', 'Rua I', 'Porto Alegre', 'RS', '65432-109', 'Brasil', '999999999999'),
('A010', 'Pedro Luiz', 'Rua J', 'Brasília', 'DF', '76543-210', 'Brasil', '11967019255');
